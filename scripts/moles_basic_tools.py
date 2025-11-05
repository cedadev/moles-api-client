"""

moles_basic_tools.py
--------------------

Package of tools used in many scripts

started 18/12/2015 by G.A. Parton

use 

from moles_basic_tools import *


"""
import sys
from typing import TypeVar, Optional, Protocol



T = TypeVar("T")

from scripts.utils import get_client
from moles_api_v_3_client.client import AuthenticatedClient

token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4ZjhmaUpyaUtDY3hmaHhzdU5vazVEekdJdFZ4amhhTWNJa05ZX2U4MnhJIn0.eyJleHAiOjE3NjE4MjA3ODMsImlhdCI6MTc2MTU2MTU4MywianRpIjoiZTI4M2M5Y2UtZTI4Ny00MmJhLTk0ZWYtMmQ2YjEwM2M5Yzc4IiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5jZWRhLmFjLnVrL3JlYWxtcy9jZWRhIiwic3ViIjoiNzhhMzRlMzYtZjM4MC00NGY2LThmZmItNTQ3NDk0OWNjYjExIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoic2VydmljZXMtcG9ydGFsLWNlZGEtYWMtdWsiLCJzZXNzaW9uX3N0YXRlIjoiZmMxZmE5M2QtYzFlMi00NTM0LWE0MjAtMGMxZDhkYTBhM2I0IiwiYWNyIjoiMSIsInNjb3BlIjoiZW1haWwgb3BlbmlkIHByb2ZpbGUgZ3JvdXBfbWVtYmVyc2hpcCIsInNpZCI6ImZjMWZhOTNkLWMxZTItNDUzNC1hNDIwLTBjMWQ4ZGEwYTNiNCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJvcGVuaWQiOiJodHRwczovL2NlZGEuYWMudWsvb3BlbmlkL0Fkcmlhbi5EZWJza2kiLCJuYW1lIjoiQWRyaWFuIERlYnNraSIsInByZWZlcnJlZF91c2VybmFtZSI6ImFkZWJza2kiLCJnaXZlbl9uYW1lIjoiQWRyaWFuIiwiZmFtaWx5X25hbWUiOiJEZWJza2kiLCJlbWFpbCI6ImFkcmlhbi5kZWJza2lAc3RmYy5hYy51ayJ9.tfi8XuXQLoHFlV4wPQ_5O185WbJ9q5UVJgv59GEucwkbCilG6kfEk0DOlEyh6X-SVFcnmpJt9-5GgyzKK8AqktG2H4lK30cfwONDAGrdjuJRxBsD1s7N38Z-eUvvabP7YDAU5kNxCodWLti3v0zUJb152cUkOkfHKhrtKKzcM__V4eYteai3tYrkEcCOQoo0935r9vAJ9w8eyIEZOJxuJgfD451bcpH1kFjBqqtipkxJGBQtIOjgsme251QGJKriswEqNN_9-GlFEH9D1U5fjQCzp2mSlUqXNo8gCuFnR9uNgkqY8nTu2OpDGHJW3ERGD2UaO28XdDLQhg602pxdWQ'
CLIENT = AuthenticatedClient(base_url='http://localhost:8000', token=token)

from moles_api_v_3_client.api.identifiers import identifiers_list
from moles_api_v_3_client.api.referenceables import referenceables_list

from moles_api_v_3_client.api.acquisitions import acquisitions_list
from moles_api_v_3_client.api.observationcollections import observationcollections_list
from moles_api_v_3_client.api.computations import computations_list
from moles_api_v_3_client.api.instruments import instruments_list
from moles_api_v_3_client.api.mpos import mpos_list
from moles_api_v_3_client.api.observations import observations_list
from moles_api_v_3_client.api.platforms import platforms_list
from moles_api_v_3_client.api.projects import projects_list
from moles_api_v_3_client.api.results import results_list

from moles_api_v_3_client.api.onlineresources import onlineresources_list, onlineresources_create
from moles_api_v_3_client.models.online_resource_write_request import OnlineResourceWriteRequest
from moles_api_v_3_client.models.observation_read import ObservationRead

from moles_api_v_3_client.api.parties import parties_create, parties_list
from moles_api_v_3_client.models.party_write_request import PartyWriteRequest
from moles_api_v_3_client.models.party_read import PartyRead

from moles_api_v_3_client.api.rpis import rpis_create, rpis_list
from moles_api_v_3_client.models.responsible_party_info_write_request import ResponsiblePartyInfoWriteRequest
from moles_api_v_3_client.models.responsible_party_info_read import ResponsiblePartyInfoRead
from moles_api_v_3_client.models.role_enum import RoleEnum

from moles_api_v_3_client.models.referenceable import Referenceable


SHORT_CODES_TO_ENDPOINTS_MAP = {
    'acq': acquisitions_list, 
    'coll': observationcollections_list,
    'comp': computations_list,
    'instr': instruments_list,
    'mpop': mpos_list,
    'ob': observations_list,
    'plat': platforms_list,
    'proj': projects_list,
    'result': results_list 
    }

import logging

logging.basicConfig(level = logging.INFO)

log = logging.getLogger(__name__)

class ApiReadReferenceable(Protocol):
    uuid: str



def _get_role_enum(value: str) -> RoleEnum:
    '''
    Helper function for getting Enum value corresponding to the given string (there's no built in function in the class)
    '''
    normalized = value.strip().lower()
    
    for role in RoleEnum:
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
    res = identifiers_list.sync_detailed(client=CLIENT, identifier_type='doi', related_to_uuid=uuid)
    
    return res.parsed.count > 0

def uuid_to_obj(uuid: str, short_code: str = None) -> ApiReadReferenceable:
    """
    Function that checks if record of given uuid exists and if so returns it
    """
    if not short_code:
        res = referenceables_list.sync_detailed(client=CLIENT, uuid=uuid)
        if res.parsed.count != 1:
            return None
        
        short_code = res.parsed.results[0].short_code
    
    list_function = SHORT_CODES_TO_ENDPOINTS_MAP[short_code]
    
    res = list_function.sync_detailed(client=CLIENT, uuid=uuid)
    
    return res.parsed.results[0]

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
                raise RuntimeError(f"API: {response.status_code}")

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
        party_type = type_of_party
    )
    res = parties_create.sync_detailed(client=CLIENT, body=model)
    if res.status_code.value != 201:
        raise RuntimeError(f'API: {res.status_code}')
    
    # convert Write object to Read object for consistency
    ob_id = res.parsed.ob_id
    res = parties_list.sync_detailed(client=CLIENT, ob_id=ob_id)
    
    
    return res.parsed.results[0]

def rpi_maker(role: str, party_ob_id: int, related_to: str, priority:int = 1) -> ResponsiblePartyInfoRead:
    model = ResponsiblePartyInfoWriteRequest(
        party = party_ob_id,
        role = _get_role_enum(role),
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
        response = rpis_list.sync_detailed(client=CLIENT, related_to_uuid=target_record_uuid, role=role)
        existing_rpi_for_role = response.parsed.results
        
        priority = response.parsed.count + 1
        
        for party in parties:
	        # first see if the party already exists, if not, then create
            # do this for Project related parties ONLY - i.e. PI, Co-I, Funder

            if party.ob_id in [rpi.party.ob_id for rpi in existing_rpi_for_role]:
                continue
            
            model = ResponsiblePartyInfoWriteRequest(
                role=_get_role_enum(role),
                party = party.ob_id,
                priority = priority,
                related_to = target_record_uuid
            )
            response = rpis_create.sync_detailed(client=CLIENT, body=model)
            
            priority += 1
