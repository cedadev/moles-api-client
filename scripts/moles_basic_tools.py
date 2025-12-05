import sys
from typing import Protocol
from enum import Enum
from collections.abc import Callable


from scripts.utils import get_client
from moles_api_v_3_client.client import AuthenticatedClient

CLIENT = get_client()
# --- Core API endpoints (by domain) ---
from moles_api_v_3_client.api.acquisitions import acquisitions_list
from moles_api_v_3_client.api.computations import computations_list
from moles_api_v_3_client.api.identifiers import identifiers_list, identifiers_partial_update
from moles_api_v_3_client.api.instruments import instruments_list
from moles_api_v_3_client.api.mpos import mpos_list
from moles_api_v_3_client.api.observationcollections import observationcollections_list
from moles_api_v_3_client.api.observations import observations_list
from moles_api_v_3_client.api.onlineresources import onlineresources_list, onlineresources_create
from moles_api_v_3_client.api.parties import parties_create, parties_list
from moles_api_v_3_client.api.platforms import platforms_list
from moles_api_v_3_client.api.projects import projects_list
from moles_api_v_3_client.api.referenceables import referenceables_list
from moles_api_v_3_client.api.results import results_list
from moles_api_v_3_client.api.rpis import rpis_create, rpis_list
from moles_api_v_3_client.api.composites import composites_list

# --- Models: core data entities ---
from moles_api_v_3_client.models.referenceable import Referenceable
from moles_api_v_3_client.models.observation_collection_read import ObservationCollectionRead
from moles_api_v_3_client.models.observation_read import ObservationRead
from moles_api_v_3_client.models.result_read import ResultRead  # (optional if used)

# --- Models: parties and roles ---
from moles_api_v_3_client.models.party_read import PartyRead
from moles_api_v_3_client.models.party_write_request import PartyWriteRequest
from moles_api_v_3_client.models.role_enum import RoleEnum
from moles_api_v_3_client.models.responsible_party_info_read import ResponsiblePartyInfoRead
from moles_api_v_3_client.models.responsible_party_info_write_request import ResponsiblePartyInfoWriteRequest
from moles_api_v_3_client.models.identifier_type_enum import IdentifierTypeEnum

# --- Models: online resources ---
from moles_api_v_3_client.models.online_resource_write_request import OnlineResourceWriteRequest

# --- Models: identifiers and misc ---
from moles_api_v_3_client.models.patched_identifier_write_request import PatchedIdentifierWriteRequest

    
SHORT_CODES_TO_ENDPOINTS_MAP = {
    'acq': acquisitions_list, 
    'cmppr': composites_list,
    'coll': observationcollections_list,
    'comp': computations_list,
    'instr': instruments_list,
    'mpop': mpos_list,
    'ob': observations_list,
    'plat': platforms_list,
    'proj': projects_list,
    'result': results_list,
    }

import logging

logging.basicConfig(level = logging.INFO)

log = logging.getLogger(__name__)

class ApiReadReferenceable(Protocol):
    ob_id: int
    uuid: str
    
def get_endpoint_by_shortcode(short_code: str) -> Callable:
    return SHORT_CODES_TO_ENDPOINTS_MAP.get(short_code, None)

def _get_value_enum(value: str, enum_class: Enum) -> Enum:
    '''
    Helper function for getting Enum value corresponding to the given string (there's no built in function in the class)
    '''
    normalized = value.strip().lower()
    
    for role in enum_class:
        if role.value.lower() == normalized:
            return role
        
    return None
    
def exit_nicely(msg: str = ""):
    '''
    Method for exiting from the app and providing traceback message
    '''
    
    import traceback

    print(__doc__)
    print(msg)
    traceback.print_exc()
    sys.exit()
    
def doi_id_checker(record: Referenceable) -> bool:
    """
    A quick function that checks to see if a DOI has been assigned to the record
    if it has, then the record should NOT be editted
    """
    uuid = record.uuid
    id_type = _get_value_enum('doi', IdentifierTypeEnum)
    response = identifiers_list.sync_detailed(client=CLIENT, identifier_type=id_type, related_to_uuid=uuid)
    
    return response.parsed.count > 0

def uuid_to_obj(uuid: str, short_code: str = None) -> ApiReadReferenceable | None:
    """
    Function that checks if record of given uuid exists and if so returns it
    """
    if not short_code:
        response = referenceables_list.sync_detailed(client=CLIENT, uuid=uuid)
        if response.parsed.count != 1:
            return None
        
        short_code = response.parsed.results[0].short_code
    
    endpoint_list = get_endpoint_by_shortcode(short_code)
    
    response = endpoint_list.sync_detailed(client=CLIENT, uuid=uuid)
    
    return response.parsed.results[0]

def get_procedure(observation: ObservationRead) -> ApiReadReferenceable:
    """
    Function to return the procedure of an observation
    """
    
    procedure = observation.procedureAcquisition or observation.procedureComputation or observation.procedureCompositeProcess
    
    uuid = procedure.uuid
    short_code = procedure.short_code
    
    procedure = uuid_to_obj(uuid, short_code)
        
    return procedure

def copy_online_resources(source_object: ApiReadReferenceable, target_object: ApiReadReferenceable) -> None:
    """
    Function to copy online resources from source object to target object
    (useful when merging records)
    """    
    s_online_resources = onlineresources_list.sync_detailed(client=CLIENT, ob_id_in=source_object.onlineresource_set)
    t_online_resources = onlineresources_list.sync_detailed(client=CLIENT, ob_id_in=target_object.onlineresource_set)

    for resource in s_online_resources.parsed.results:
        if not any(resource.linkage == r.linkage for r in t_online_resources.parsed.results):
            model = OnlineResourceWriteRequest(
                linkage = resource.linkage,
                name = resource.name,
                related_to = target_object.uuid
            )
            response = onlineresources_create.sync_detailed(client=CLIENT, body=model)
            
            if response.status_code.value != 201:
                raise RuntimeError(f"API: {response.status_code.value}")

def party_maker(party_first: str, party_last: str) -> PartyRead:
    """
    function to create a new Party record as needed
    """
    type_of_party = 'individual'

    if not party_first:
        type_of_party = 'organisation'
     
    model = PartyWriteRequest(
        first_name = party_first,
        last_name = party_last,
        party_type = type_of_party,
        address_line_1 = ' ', # temporary placeholder, client needs to be fixed
        address_line_2 = ' '
    )
    res = parties_create.sync_detailed(client=CLIENT, body=model)
    if res.status_code.value != 201:
        raise RuntimeError(f'API: {res.status_code.value}')
    
    # convert Write object to Read object for consistency
    ob_id = res.parsed.ob_id
    res = parties_list.sync_detailed(client=CLIENT, ob_id=ob_id)
    
    
    return res.parsed.results[0]

def rpi_maker(role: str, party_ob_id: int, related_to: str, priority:int = 1) -> ResponsiblePartyInfoRead:
    model = ResponsiblePartyInfoWriteRequest(
        party = party_ob_id,
        role = _get_value_enum(role, RoleEnum),
        priority=priority,
        related_to=related_to
    )
    res = rpis_create.sync_detailed(client=CLIENT, body=model)
    ob_id = res.parsed.ob_id
    res = rpis_list.sync_detailed(client=CLIENT, ob_id=ob_id)
    
    return res.parsed.results[0]

def party_check_create(party_name: str) -> PartyRead:
    
    party_last = party_name[0].strip()
    if len(party_name) == 2:
        party_first = party_name[1].strip()
    else:
        party_first = ''

    res = parties_list.sync_detailed(client=CLIENT, last_name=party_last, first_name=party_first)
    if res.parsed.count > 0:
        return res.parsed.results[0]
    
    res = parties_list.sync_detailed(client=CLIENT, last_name=party_last, first_name_startswith=party_first)
    if res.parsed.count > 0:
        return res.parsed.results[0]
    
    log.error("")
    return party_maker(party_first, party_last) 

def add_parties(party_dict: dict[str, list[PartyRead]], target_record_uuid: str) -> None:
    """
        function to add related party info to the specified record
        check for existing parties doing role
        get priority level
        check that not duplicating entry 
    """

    for role, parties in party_dict.items():
        response = rpis_list.sync_detailed(client=CLIENT, related_to_uuid=target_record_uuid, role=_get_value_enum(role, RoleEnum))
        existing_rpi_for_role = response.parsed.results
        
        priority = response.parsed.count + 1
        
        for party in parties:
	        # first see if the party already exists, if not, then create
            # do this for Project related parties ONLY - i.e. PI, Co-I, Funder

            if party.ob_id in [rpi.party.ob_id for rpi in existing_rpi_for_role]:
                continue
            
            model = ResponsiblePartyInfoWriteRequest(
                role=_get_value_enum(role, RoleEnum),
                party = party.ob_id,
                priority = priority,
                related_to = target_record_uuid
            )
            response = rpis_create.sync_detailed(client=CLIENT, body=model)
            
            priority += 1

def copy_party_by_role(source_object: ApiReadReferenceable, target_object: ApiReadReferenceable, role: str) -> None:
    """
    quick function to copy parties doing a specific role from source object to target object
    (useful when merging records)
    """

    res = rpis_list.sync_detailed(client=CLIENT, role=_get_value_enum(role, RoleEnum), related_to_uuid=source_object.uuid)
    source_parties = [rpi.party for rpi in res.parsed.results]
    party_dict = {role: source_parties}
    
    add_parties(party_dict, target_object.uuid)
   
def move_identifiers(source_object: ApiReadReferenceable, target_object: ApiReadReferenceable) -> None:
    """
    Function to copy online resources from source object to target object
    (useful when merging records)
    """    
    res = identifiers_list.sync_detailed(client=CLIENT, related_to_uuid=source_object.uuid)
    s_identifiers = res.parsed.results
    
    for identifier in s_identifiers:
        model = PatchedIdentifierWriteRequest(
            related_to=target_object.uuid
        )
        res = identifiers_partial_update.sync_detailed(client=CLIENT, ob_id=identifier.ob_id, body=model)
    
def get_primary_obs_for_collection(obs_col: ObservationCollectionRead, pub_level: int = 1, unique: bool = True) -> list:
    """
    find observations which cite the project pointing to the collection
    and which are either published or citable

    """
    obs_col_project_set = obs_col.project_set
    primary_obs = []
    
    publication_status = ['published', 'citable']
    if pub_level != 1:
        publication_status += ['working', 'obsolete', 'historic']
    
    if not obs_col_project_set:
        log.warning('this does not have proj set: %s',obs_col.uuid)
        return primary_obs
        
        
    res = observations_list.sync_detailed(client=CLIENT, ob_id_in=obs_col.member)
    observations = res.parsed.results
    
    for ob in observations:
        #first check is that it is a primary observation within the set, i.e. not a third party obs
        primary_proj_listed = 0
        
        for ob_proj in ob.projects:
            if ob_proj.ob_id in obs_col_project_set:
                primary_proj_listed = 1
                break
        
        
        if not primary_proj_listed:
            continue
        
        if not ob.publicationState in publication_status:
            continue
        
        if not unique:
            primary_obs.append(ob)
            continue
        
        res = results_list.sync_detailed(client=CLIENT, data_path=ob.result_field.data_path)
        if res.parsed.count != 1:
            log.warning(ob.result_field.internalPath)
            continue
        
        primary_obs.append(ob)
                   
                        
    return primary_obs
