import logging
log = logging.getLogger(__name__)


from scripts.utils import get_client
from scripts import moles_basic_tools as mbt

from moles_api_v_3_client.api.parties import parties_list
from moles_api_v_3_client.api.projects import projects_create
from moles_api_v_3_client.api.identifiers import identifiers_list

from moles_api_v_3_client.models.project_write_request import ProjectWriteRequest, PublicationState6F9Enum, StatusEnum

CLIENT = get_client()

def poppy_organisation_mappings(name):

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
    res = parties_list.sync_detailed(client=CLIENT, ob_id=ob_id)
    
    if res.status_code.value != 200:
        log.error('API ERROR > %r', res.status_code)
        return None
    
    if res.parsed.count < 1:
        log.error('NOT FOUND! > %r %r' , name, poppy_org_dict[name] ) 
        return None
    
    return res.parsed.results[0]


def party_check_create_faam(party_name):
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


def get_faam_project(project_abbrev_upper):
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
        raise "too many matches!!! for %s"% project_abbrev_upper
    
    
    with open('new_proj_list', 'a') as new_proj_file:
    
        new_proj_details = {'abstract': f'The {project_abbrev_upper} project utilised the FAAM aircraft. Further details to follow.',
                            #,'imageDetails': None # imageDetails - if funder is NERC then choose NERC logo
                            'keywords': f' {project_abbrev_upper }, FAAM, Met Office',
                            'publicationState': 'working', # set to working
                            'status': 'completed', # set to completed.. remember this is a controlled list, with mapping between the value and user wording!
                            'title': f'{project_abbrev_upper} FAAM Aircraft Project'
                            }
        
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

        mbt.add_parties(proj_party_dict, new_proj_record)

        id_details = {'relatedTo': new_proj_record
                        ,'identifierType': 'ceda_abbreviation'
                        ,'url': project_abbrev_upper.strip()
                        }
        id_added = Identifier.objects.create(**id_details)

        
        new_proj_file.write('%s|http://catalogue.ceda.ac.uk/uuid/%s\n'% (project_abbrev_upper, new_proj_record.uuid) )
        log.info('New project record created > %r http://catalogue.ceda.ac.uk/uuid/%r', new_proj_record.title, new_proj_record.uuid)
