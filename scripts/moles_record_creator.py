
from moles_api_v_3_client.api.observations import observations_create
from moles_api_v_3_client.models.observation_write_request import ObservationWriteRequest, StatusEnum, PublicationStateCbbEnum, UpdateFrequencyEnum
from moles_api_v_3_client.models.observation_write import ObservationWrite

from moles_api_v_3_client.api.results import results_create
from moles_api_v_3_client.models.result_write_request import ResultWriteRequest, CurationCategoryEnum, StorageLocationEnum, StorageStatusEnum

from moles_api_v_3_client.api.verticalextents import verticalextents_create
from moles_api_v_3_client.models.vertical_extent_write_request import VerticalExtentWriteRequest

from moles_api_v_3_client.api.dqconformanceresults import dqconformanceresults_create
from moles_api_v_3_client.models.dq_conformance_result_write_request import DQConformanceResultWriteRequest

from moles_api_v_3_client.api.times import times_create
from moles_api_v_3_client.models.time_period_request import TimePeriodRequest

from moles_api_v_3_client.api.bboxes import bboxes_create
from moles_api_v_3_client.models.geographic_bounding_box_write_request import GeographicBoundingBoxWriteRequest

from moles_api_v_3_client.api.onlineresources import onlineresources_create
from moles_api_v_3_client.models.online_resource_write_request import OnlineResourceWriteRequest, FunctionEnum

from moles_api_v_3_client.api.projects import projects_list, projects_create
from moles_api_v_3_client.models.project_write_request import ProjectWriteRequest
from moles_api_v_3_client.models.project_write import ProjectWrite
from moles_api_v_3_client.models.publication_state_6f9_enum import PublicationState6F9Enum

from moles_api_v_3_client.api.rpis import rpis_create
from moles_api_v_3_client.models.responsible_party_info_write_request import ResponsiblePartyInfoWriteRequest
from moles_api_v_3_client.models.role_enum import RoleEnum

from moles_api_v_3_client.api.parties import parties_list, parties_create
from moles_api_v_3_client.models.party_write_request import PartyWriteRequest, PartyTypeEnum
from moles_api_v_3_client.models.party_read import PartyRead
from moles_api_v_3_client.models.party_write import PartyWrite

from moles_api_v_3_client.api.acquisitions import acquisitions_create
from moles_api_v_3_client.models.procedure_acquisition_write_request import ProcedureAcquisitionWriteRequest
from moles_api_v_3_client.models.procedure_acquisition_write import ProcedureAcquisitionWrite

from moles_api_v_3_client.api.instruments import instruments_create
from moles_api_v_3_client.models.instrument_write_request import InstrumentWriteRequest

from moles_api_v_3_client.api.computations import computations_create
from moles_api_v_3_client.models.procedure_computation_write_request import ProcedureComputationWriteRequest
from moles_api_v_3_client.models.procedure_computation_write import ProcedureComputationWrite

from moles_api_v_3_client.api.composites import composites_create
from moles_api_v_3_client.models.procedure_composite_process_write_request import ProcedureCompositeProcessWriteRequest


from moles_api_v_3_client.types import Response, UNSET
from scripts.utils import get_client
import datetime
import sys
import re
from typing import Callable, TypeAlias, Protocol, Union
from scripts.moles_basic_tools import uuid_to_obj, ApiReadReferenceable, _get_value_enum

ROLL_BACK_LIST = []

PartyObj = Union[
    PartyRead,
    PartyWrite
]

WriteObj = Union[
    ObservationWriteRequest,
    ResultWriteRequest,
    VerticalExtentWriteRequest,
    DQConformanceResultWriteRequest,
    TimePeriodRequest,
    GeographicBoundingBoxWriteRequest,
    OnlineResourceWriteRequest,
    ProjectWriteRequest,
    ResponsiblePartyInfoWriteRequest,
    PartyWriteRequest,
    ProcedureAcquisitionWriteRequest,
    InstrumentWriteRequest,
    ProcedureComputationWriteRequest,
    ProcedureCompositeProcessWriteRequest
]

class CreateModule(Protocol):
    def sync_detailed(self, body: object) -> Response:
        pass

class RecordCreationError(Exception):
    pass


def _validate_api_response(response: Response, expected_status_code: int, message: str = '') -> None:
    status_code = response.status_code.value
    if status_code != expected_status_code:
        print(message)
        if status_code == 500:
            raw = str(response.content)
            clean = raw.lstrip("b'").rstrip("'").replace("\\n", "")
            with open('error.html', 'w') as f:
                f.write(clean)
        raise Exception(response)

def _validate_record_url(url: str) -> None:
    if 'catalogue.ceda.ac.uk' not in url or 'admin' in url : 
        raise RecordCreationError('Record URL needs to be a valid user-view MOLES record, not external URL. Exiting and cleaning up...')

def url_to_obj(url: str, short_code: str = '') -> ApiReadReferenceable | None:
    # check if there's uuid in the url
    match = re.search('/([\da-f]{32})/?$', url)
    if not match:
        return None
    
    # prevent people from trying to use a non MOLES link
    _validate_record_url(url)
    
    uuid = match.group(1)
    return uuid_to_obj(uuid, short_code)

def create_obj(create_fn: CreateModule, write_obj: WriteObj) -> Response:
    """function to make a moles object """
    
    # get name for logging 
    func_name = create_fn.__name__
    model_name = func_name.split('_')[0]
    print(f'Creating {model_name} object')
    
    response: Response = create_fn.sync_detailed(client=CLIENT, body=write_obj)
    
    _validate_api_response(response, 201)
    
    print(f"Created succesfully {response.parsed.ob_id}")
    
    ROLL_BACK_LIST.append((model_name, response.parsed.ob_id))

    return response

def party_check_create(last_name: str, first_name: str = '') -> PartyObj | None:
    """Create or find a party. If first_name is not given an organisation party is made. If a party that matches can be found then it is returned."""    
    if not last_name:
        return None
    
    print(last_name)
    last_name = last_name.strip()
    first_name = first_name.strip()
    
    party_type = PartyTypeEnum.INDIVIDUAL if first_name else PartyTypeEnum.ORGANISATION 
    first_name = first_name or UNSET

    response = parties_list.sync_detailed(client=CLIENT, last_name=last_name, first_name=first_name)
    _validate_api_response(response, 200)
    
    if response.parsed.count > 0:
        return response.parsed.results[0]
    
    new_party = create_obj(
            parties_create,
            PartyWriteRequest(
                first_name=first_name,
                last_name=last_name,
                party_type=party_type
            )
        )
    return new_party.parsed

def make_project(proj_title: str, proj_abstract: str, ceda_officer: PartyObj, funder: PartyObj = None, pi: PartyObj = None) -> ProjectWrite:
    """
    Creates  project record
    """
    response = create_obj(
        projects_create,
        ProjectWriteRequest(
            title=proj_title,
            abstract=proj_abstract,
            publication_state=PublicationState6F9Enum.PUBLISHED,
            status=StatusEnum.COMPLETED
        )
    )
    new_proj = response.parsed
    
    rpis_to_create = [
        ('ceda_officer', ceda_officer),
        ('funder', funder),
        ('principal_investigator', pi)
    ]
    
    for role, party in rpis_to_create:
        if not party:
            continue
            
        role = _get_value_enum(role, RoleEnum)
        
        create_obj(
            rpis_create,
            ResponsiblePartyInfoWriteRequest(
                role=role,
                party=party.ob_id,
                priority=1,
                related_to=new_proj.uuid
            )
        )

    return new_proj

def make_acquisition(inst_info: dict, obs_title: str, ceda_officer: int) -> ProcedureAcquisitionWrite:
    if not inst_info:
        return None
    
    if not (inst_info.get('catalogue_url') or inst_info.get('title')):
        raise RecordCreationError('Blank instrument details given in yaml file. Exiting and cleaning up...')
        
    
    if "catalogue_url" in inst_info and inst_info["catalogue_url"]:
        # get instr
        inst = url_to_obj(inst_info["catalogue_url"], 'inst')
        
    else: 
        # create inst
        desc = inst_info.get('description', '')
        inst = create_obj(
            instruments_create,
            InstrumentWriteRequest(
                title=inst_info["title"],
                abstract=desc
            )
        )
        
        # rpi for inst
        create_obj(
            rpis_create,
            ResponsiblePartyInfoWriteRequest(
                role=RoleEnum.CEDA_OFFICER,
                party=ceda_officer,
                priority=1,
                related_to=inst.parsed.uuid
            )
        )
    
    # create acq
    acquisition = create_obj(
        acquisitions_create,
        ProcedureAcquisitionWriteRequest(
            title=f"Acquisition for: {obs_title}",
            independent_instrument=inst.ob_id
        )
    )
    
    # rpi for acq
    create_obj(
        rpis_create,
        ResponsiblePartyInfoWriteRequest(
            role=RoleEnum.CEDA_OFFICER,
            party=ceda_officer,
            priority=1,
            related_to=acquisition.parsed.uuid
        )
    )

    return acquisition.parsed
    
def make_computation(comp_info: dict, obs_title: str, ceda_officer: int) -> ProcedureComputationWrite:
    if not comp_info:
        return None
    
    if not (comp_info.get('catalogue_url') or comp_info.get('title')):
        raise RecordCreationError('Blank instrument details given in yaml file. Exiting and cleaning up...')
    
    if "catalogue_url" in comp_info and comp_info["catalogue_url"]:
        comp = url_to_obj(comp_info["catalogue_url"], 'comp')

    else:
        desc = comp_info.get('description', '')
        comp = create_obj(
            computations_create,
            ProcedureComputationWriteRequest(
                title=comp["title"],
                abstract=desc
            )
        )
        
        # rpi for inst
        create_obj(
            rpis_create,
            ResponsiblePartyInfoWriteRequest(
                role=RoleEnum.CEDA_OFFICER,
                party=ceda_officer,
                priority=1,
                related_to=comp.parsed.uuid
            )
        )
        
    # add online resources to comp
    if "docs" in comp_info:
        for ores in comp_info["docs"]:
            create_obj(
                onlineresources_create,
                OnlineResourceWriteRequest(
                    linkage=ores['url'],
                    function=FunctionEnum.DOCUMENTATION,
                    name=ores['title'],
                    related_to=comp.parsed.uuid
                )
            )
        
    return comp.parsed

def make_new_basic_obs_record(obs_dict):

    """title, abstract, result_path, format, n_files, size,
                              existing_project_url, new_project_title, new_project_abstract,
                              ceda_officer_first, ceda_officer_last, 
                              authors_list, links_list, data_quality, lineage, 
                              start_time, end_time, north, south, east, west, funder_name, 
                              pi_first, pi_last):
    """
    # list of django objects to delete if there is a problem
    delete_if_problem = []

    # make a new ob record
    print(StatusEnum.COMPLETED)
    print(PublicationStateCbbEnum.PREVIEW)
    print(datetime.datetime.now())
    print(UpdateFrequencyEnum.NOTPLANNED)
    print("Licence and acess control done in Access Control system")

    image_details = UNSET
    if obs_dict.get('logo'):
        image_details = [obs_dict['logo']]
        
    vertical_extent = UNSET
    if obs_dict.get('vertical_extent'):
        ve = obs_dict.get('vertical_extent')
        if 'highest_level_bound' in ve and 'lowest_level_bound' in ve and 'units' in ve:
            response = create_obj(
                verticalextents_create,
                VerticalExtentWriteRequest(
                    highest_level_bound=ve.get('highest_level_bound', 0),
                    lowest_level_bound=ve.get('lowest_level_bound', 0),
                    units=ve.get('units', '')
                    )
                )
            vertical_extent = response.parsed.ob_id
        
        else:
            print("Invalid 'vertical extent' format")
            
    
    result = UNSET
    if 'result_path' in obs_dict:
        response = create_obj(
            results_create,
            ResultWriteRequest(
                data_path=obs_dict["result_path"],
                curation_category=CurationCategoryEnum.A,
                file_format=obs_dict["format"],
                storage_location=StorageLocationEnum.INTERNAL,
                storage_status=StorageStatusEnum.ONLINE
                )
            )
        result = response.parsed.ob_id
        
        
    dqs = UNSET
    if 'quality' in obs_dict:
        response =  create_obj(
            dqconformanceresults_create,
            DQConformanceResultWriteRequest(
                explanation = obs_dict['quality']
            )
        )
        dqs = response.parsed.ob_id
        
    
    timerange = UNSET
    if 'time_range' in obs_dict:
        tr = obs_dict['time_range']
        if 'start' in tr and 'end' in tr:
            response = create_obj(
                times_create, 
                TimePeriodRequest(
                    start_time=obs_dict['start'],
                    end_time=obs_dict['end']
                )
            )
            timerange = response.parsed.ob_id


    bbox = UNSET
    if 'bbox' in obs_dict:
        bb = obs_dict['bbox']
        response = create_obj(
            bboxes_create,
            GeographicBoundingBoxWriteRequest(
                east_bound_longitude=bb['east'],
                west_bound_longitude=bb['west'],
                north_bound_latitude=bb['north'],
                south_bound_latitude=bb['south'],
            )
        )
    
    
    #######      
            
    # make a new project
    if not (obs_dict.get("ceda_officer")):
        raise RecordCreationError("Missing ceda_officer")
    
    ceda_officer = party_check_create(obs_dict["ceda_officer"]["surname"], obs_dict["ceda_officer"]["firstname"])
    project = obs_dict.get("project")
    
    if project:
        proj = url_to_obj(project["catalogue_url"], 'proj')
        
        if not proj:
            funder = party_check_create(project.get('funder'))
            pi_dict = project.get('PI', {})
            pi = party_check_create(pi_dict.get('surname'), pi_dict.get('firstname'))
            proj = make_project(project["title"], project["description"], ceda_officer, funder=funder, pi=pi)


    ceda_officer
    
    # make an aquisition
    acquisition = make_acquisition(inst_info=obs_dict.get("instrument"), obs_title=obs_dict['title'], ceda_officer=ceda_officer.ob_id)
    acquisition = UNSET if acquisition is None else acquisition.ob_id
    
    computation = make_computation(comp_info=obs_dict.get("computation"), obs_title=obs_dict['title'], ceda_officer=ceda_officer.ob_id)
    computation = UNSET if computation is None else computation.ob_id
    
    composite_process = UNSET
    
    if acquisition != UNSET and acquisition != UNSET:
        yn = input("STOP!!! This has both an Acquisition AND Computation Process. Want to switch to a Compsotite Process? [y/n]? >   ")

        if yn.startswith('y'):
            compo = create_obj(
                composites_create,
                ProcedureCompositeProcessWriteRequest(
                    title=f'Composite Process for {obs_dict['title']}',
                    abstract=f'Composite process covering {acquisition.title} and {computation.title}.',
                    acquisition_component=acquisition.ob_id,
                    computation_component=computation.ob_id
                )
            )

            # rpi for inst
            create_obj(
                rpis_create,
                ResponsiblePartyInfoWriteRequest(
                    role=RoleEnum.CEDA_OFFICER,
                    party=ceda_officer,
                    priority=1,
                    related_to=compo.parsed.uuid
                )
            )
            acquisition = UNSET
            computation = UNSET
            composite_process = compo
        else:
            print('OK, you will need to look at this manually')
            # rollback()
            # sys.exit()

    
    
    
    
    ##### CREATE OBS
    
    response = create_obj(
        observations_create,
        ObservationWriteRequest(
            title=obs_dict.get("title", ''),
            abstract=obs_dict.get("description", ""),
            status=StatusEnum.COMPLETED,
            publication_state=PublicationStateCbbEnum.PREVIEW,
            update_frequency=UpdateFrequencyEnum.NOTPLANNED,
            data_lineage=obs_dict.get("lineage"),
            non_geographic_flag=True,
            resolution=obs_dict.get("resolution", ""),
            keywords=obs_dict.get("keywords", ""),
            image_details=image_details,
            vertical_extent=vertical_extent,
            result_field=result,
            result_quality=dqs,
            time_period=timerange,
            geographic_extent=bbox,
            procedure_acquisition = acquisition,
            procedure_computation = computation,
            procedure_composite_process = composite_process
        )
    )
    
    obs:  ObservationWrite = response.parsed
    
    
    # add online resources
    if "docs" in obs_dict:
        for doc in obs_dict["docs"]:
            response = create_obj(
                onlineresources_create,
                OnlineResourceWriteRequest(
                    linkage=doc['url'],
                    function=FunctionEnum.DOCUMENTATION,
                    name=doc['title'],
                    related_to=obs.uuid
                )
            )
    
    
    create_obj(
        rpis_create, 
        ResponsiblePartyInfoWriteRequest(
            role=RoleEnum.CEDA_OFFICER,
            party=ceda_officer.ob_id,
            priority=1,
            related_to=obs.uuid
        )
    )
    
    i = 1
    for a in obs_dict.get("authors", []):
        author = party_check_create(a.get('surname'), a.get('firstname'))
        create_obj(
            rpis_create,
            ResponsiblePartyInfoWriteRequest(
                role = RoleEnum.AUTHOR,
                party = author.ob_id,
                priority = i,
                related_to = obs.uuid
            )
        )
        i += 1


    print(f'View resulting Observation record at: https://catalogue.ceda.ac.uk/admin/cedamoles_app/observation/{obs}/')
    
    
def main():
    global CLIENT
    CLIENT = get_client()
    
    obs_dict = {
        'title': f'titleTest{datetime.datetime.now()}',
        'description': 'abstract',
        'lineage': 'lineage',
        'resolution': 'reseseses',
        'vertical_extent': {
            'highest_level_bound': 1,
            'lowest_level_bound': 0,
            'units': 'C'
        },
        'ceda_officer':
            {
                'surname': 'Example Org',
                'firstname': ''
            }
    }
    make_new_basic_obs_record(obs_dict)

if __name__ == '__main__':
    main()