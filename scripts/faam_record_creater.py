import logging
log = logging.getLogger(__name__)

from itertools import zip_longest
import csv


from scripts.utils import get_client
from scripts import moles_basic_tools as mbt
from scripts.moles_basic_tools import ApiReadReferenceable

from moles_api_v_3_client.api.parties import parties_list
from moles_api_v_3_client.api.projects import projects_create, projects_list
from moles_api_v_3_client.api.identifiers import identifiers_list, identifiers_create
from moles_api_v_3_client.api.referenceables import referenceables_list

from moles_api_v_3_client.models.identifier_write_request import IdentifierWriteRequest
from moles_api_v_3_client.models.identifier_type_enum import IdentifierTypeEnum

from moles_api_v_3_client.models.party_read import PartyRead
from moles_api_v_3_client.models.project_read import ProjectRead

from moles_api_v_3_client.models.project_write_request import ProjectWriteRequest, PublicationState6F9Enum, StatusEnum

CLIENT = get_client()

def _check_api_response(response, expected_status_code: int, message: str = '') -> None:
    if response.status_code.value == expected_status_code:
        return
    
    print(message)
    raise Exception(f"API: {response.status_code}")
    

def poppy_organisation_mappings(name: str) -> PartyRead:

    name = name.upper()
    
    poppy_org_dict = {
        'FAAM': 15,
        'BAE SYSTEMS': 1531,
        'LEEDS': 16,
        'LEICESTER': 399,
        'READING': 80,
        'NERC': 11,
        'MET OFFICE': 5,
        'EUMETSAT': 234,
        'EUFAR': 154,
        'CEH EDINBURGH': 409,
        'UNIVERSITY OF MANCHESTER': 65,
        'LAQUILLE': 1532,
        'MANCHESTER': 65,
        'UEA': 340,
        'YORK': 249,
        'BADC': 1,
        'CEDA': 3134
    }

    
    if name not in poppy_org_dict:
        return None
    
    ob_id = poppy_org_dict[name]
    response = parties_list.sync_detailed(client=CLIENT, ob_id=ob_id)
    
    _check_api_response(response, 200)
    
    if response.parsed.count < 1:
        log.error('NOT FOUND! > %r %r' , name, poppy_org_dict[name] ) 
        return None
    
    party = response.parsed.results[0]
    
    return party

def party_check_create_faam(party_name: str) -> PartyRead:
    party_last = party_name[0].strip()
    if len(party_name) == 2:
        party_first = party_name[1].strip()
    else:
        party_first = ''


    if not party_first:
        log.info( 'checking for org in org list.... %r', party_last)
        
        return poppy_organisation_mappings(party_last)
    
    
    res = parties_list.sync_detailed(client=CLIENT, last_name=party_last, first_name=party_first)
    if res.parsed.count > 0:
        return res.parsed.results[0]
    
    res = parties_list.sync_detailed(client=CLIENT, last_name=party_last, first_name_startswith=party_first)
    if res.parsed.count > 0:
        return res.parsed.results[0]
    
    log.error("")
    return mbt.party_maker(party_first, party_last)  

def get_faam_project(project_abbrev_upper: str) -> ProjectRead:
    """
    function to make new FAAM Project record and note list of new ones made to later population
    
    note - it first checks that isn't already a MOLES Project record using the abbreviation
     
    """

    new_proj_record = None
    
    # first, lets see if we can track one down by project abbreviation only...
    
    proj_by_id_matcher = identifiers_list.sync_detailed(client=CLIENT, url_iexact=project_abbrev_upper, related_to_short_code='proj')
    if proj_by_id_matcher.parsed.count == 1:
        return proj_by_id_matcher.parsed.results[0]
    
    if proj_by_id_matcher.parsed.count > 1:
        raise Exception("too many matches!!! for %s"% project_abbrev_upper)
    
    
    with open('new_proj_list', 'a') as new_proj_file:
        model = ProjectWriteRequest(
            title=f'{project_abbrev_upper} FAAM Aircraft Project',
            abstract=f'The {project_abbrev_upper} project utilised the FAAM aircraft. Further details to follow.',
            keywords=f' {project_abbrev_upper }, FAAM, Met Office',
            publication_state=PublicationState6F9Enum.WORKING,
            status=StatusEnum.COMPLETED
        )

        res = projects_create.sync_detailed(client=CLIENT, body=model)
        
        new_proj_record = res.parsed

        proj_party_dict  = {}
        
        proj_party_dict['ceda_officer'] = [('Garland','Wendy')]

        # having determined our parties, throw this into the add_parties function to add the related parties 

        mbt.add_parties(proj_party_dict, new_proj_record.uuid)

        id_details = IdentifierWriteRequest(
            related_to= new_proj_record,
            identifier_type= mbt._get_value_enum('ceda_abbreviation', IdentifierTypeEnum),
            url=project_abbrev_upper.strip()
        )
        identifier_response = identifiers_create.sync_detailed(client=CLIENT, body=id_details)
        _check_api_response(identifier_response, 201, "Error while creating identifier record")

        
        new_proj_file.write('%s|http://catalogue.ceda.ac.uk/uuid/%s\n'% (project_abbrev_upper, new_proj_record.uuid) )
        log.info('New project record created > %r http://catalogue.ceda.ac.uk/uuid/%r', new_proj_record.title, new_proj_record.uuid)
        
        response = projects_list.sync_detailed(client=CLIENT, uuid=new_proj_record.uuid)
        _check_api_response(response, 200)
        proj_record = response.parsed.results[0]
        return proj_record

def proj_maker(project_abbrev: str, project_details: dict) -> ProjectRead:

    """
    call is made with some outline details and then creates new project record as needed
    
    Available info is:
        {'title' : title_string
        , 'abstract' : abstract_string
        , 'faam_site_url' : row[2]
        , 'moles_project_record_url' : moles_proj_uuid
        , 'pi_last' : row[4]
        , 'pi_first' : row[5]
        , 'funder' : row[6]
        , 'other' : row[7:] 
        'moles_ob_id': proj_ob_id                                   
        }


    once created we wimply need to return the Project object ID 
        
    """
    log.info("CREATING NEW PROJECT")
    
    model = ProjectWriteRequest(
        abstract=project_details.get('abstract'),
        keywords=f" {project_abbrev}, FAAM, Met Office",
        publication_state='working',
        status='completed',
        title=project_details.get('title', 'FAAM PROJECT TITLE NEEDED - %(date)s-%(time)s'), # insert date-time ?
        parent_project=project_details.get('parent_project', None)
    )
    
    # now create the record and return the project_id so that it can be linked to the record.
    
    response = projects_create.sync_detailed(client=CLIENT, body=model)
    _check_api_response(response, 201, "Error occured during creation of project record")
    
    faam_proj = response.parsed
        
    
    # to add    
    # ceda_abbreviation  = proj_abbrev
    
    party_dict = {
        'ceda_officer': [('Garland','Wendy')]
    }
    
    #make up other party_dict entries where these are supplied...
    
    def extract_name_pairs(last_str: str, first_str: str):
        """Return list of (last, first) tuples from newline-separated strings."""
        last_names = last_str.split('\n')
        first_names = first_str.split('\n')
        return list(zip_longest(last_names, first_names, fillvalue=""))
    
    prefix_to_role = [
        ("pi", "principal_investigator"),
        ("coi", "co_investigator")
    ]
    
    for prefix, key in prefix_to_role:
        last = project_details.get(f"{prefix}_last")
        first = project_details.get(f"{prefix}_first")

        if last:
            party_dict[key] = extract_name_pairs(last, first)


    party_dict['funder'] = [
        (name, "")
        for name in project_details.get("funder", "").split("\n")
        if name
    ]
    
    # having determined our parties, throw thwwwwis into the add_parties function to add the related parties 
    mbt.add_parties(party_dict, faam_proj)
    
    
    response = projects_list.sync_detailed(client=CLIENT, uuid=faam_proj.uuid)
    _check_api_response(response, 200)
    
    faam_proj = response.parsed.results[0]
            
    return faam_proj


def proj_updater(project_details):
    """
    Never implemented
    """
    pass


def faam_projects():
    """
    
    """
    
    faam_proj_list_in = 'faam_project_list.csv'
    
    proj_lines = {}
    
    parent_project_dict = {
        'EUFAR': 'a0aebebc95412cadd236706b90419153',
        'Met Office FAAM Campaigns': 'ae9d95078716251c53c396cf5b24941e',
        'Met Office Flights': 'ae9d95078716251c53c396cf5b24941e'
    }
    
    response = projects_list.sync_detailed(client=CLIENT, uuid_in=list(parent_project_dict.values()))
    _check_api_response(response, 200) 
    parent_projs = response.parsed.results
    
    # replacing uuids with proj records
    for name, uuid in parent_project_dict.items():
        for proj in parent_projs:
            if proj.uuid == uuid:
                parent_project_dict[name] = proj
    
    
    with open(faam_proj_list_in, 'rb') as csvfile:
        proj_stuff = csv.reader(csvfile)
        
        for row in proj_stuff:
            log.debug(row)
            
         
            if row[0] == 'Abbreviated title' or row == '':
                continue
                
            title_string = ''
            abstract_string = ''      
            moles_proj_uuid = None
            proj_ob = None    
            
            # Extract primary key early
            row_key = row[0].strip()

            # --- 1. If we already have a project UUID, resolve that path immediately ---

            existing_uuid = row[4].strip()

            if existing_uuid:
                log.debug(existing_uuid)

                uuid_from_url = (
                    existing_uuid.replace('http://catalogue.ceda.ac.uk/uuid/', '')
                    if "http" in existing_uuid
                    else existing_uuid
                )

                log.debug("uuid is", uuid_from_url)

                proj_ob = Project.objects.get(uuid__exact=uuid_from_url)
                

                proj_lines[row_key] = proj_ob
                continue


            # --- 2. Build title ---

            title_string = (
                row[1].decode('cp1252').encode('utf-8')
                if row[1].strip()
                else f"{row[0]} Project Details"
            )


            # --- 3. Build abstract with fallback chain ---

            abstract_string = row[2].decode('cp1252').encode('utf-8')

            if not abstract_string:
                abstract_string = (
                    "Project details needed. Please contact CEDA for additional information."
                )

            if not abstract_string:
                abstract_string = "Need to write an abstract"


            # --- 4. Resolve parent project ---

            parent_key = row[5].strip()

            if not parent_key:
                parent_project = None
            else:
                # First try cached lookup
                parent_project = parent_project_dict.get(parent_key)

                if parent_project is None:
                    parent_uuid = (
                        parent_key.replace('http://catalogue.ceda.ac.uk/uuid/', '')
                        if "http" in parent_key
                        else parent_key
                    )
                    try:
                        parent_project = Project.objects.get(uuid__exact=parent_uuid)
                    except Project.DoesNotExist:
                        parent_project = None  # Or handle differently if needed


            # --- 5. Build project details ---

            proj_details = {
                'title': title_string,
                'abstract': abstract_string,
                'faam_site_url': row[3],
                'moles_project_record_url': moles_proj_uuid,
                'parent_project': parent_project,
                'pi_last': row[6],
                'pi_first': row[7],
                'funder': row[8],
                'coi_last': row[9],
                'coi_first': row[10],
                'poc_last': row[11],
                'poc_first': row[12],
                'location_name': row[13],
                'moles_ob_id': proj_ob,
            }

            # --- 6. Create the project ---

            try:
                proj_ob = proj_maker(row[0], proj_details)
            except Exception:
                # Handle creation issues explicitly — or skip like before
                continue

            proj_lines[row_key] = proj_ob
