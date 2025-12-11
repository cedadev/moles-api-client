from scripts.imports.api import *
from scripts.imports.models import *
from scripts.utils import get_client
from scripts.moles_basic_tools import uuid_to_obj, ApiReadReferenceable, _get_value_enum

from moles_api_v_3_client.types import Response, UNSET
import datetime
import re
import json
import logging
from collections import defaultdict
import importlib
from pathlib import Path

ROLL_BACK_PATH = Path(__file__).resolve().parent / 'files' / 'rollback.json'
ROLL_BACK_DICT = defaultdict(list)
MAX_SESSIONS_NUMBER = 20

logger = logging.getLogger(__name__)

### TYPING CLASSES
# ======================= #
from typing import Protocol, Union

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

class APIWriteResponse(Protocol):
    '''
    Generic typing class for objects like ObservationWrite, ProjectWrite...
    '''
    ob_id: int

class RecordCreationError(Exception):
    pass

# ======================= #

def add_to_rollback(endpoint: str, ob_id: int):
    '''
    Function to add endpoint and ob_id to the rollback file under current session
    
    :param endpoint: Endpoint name
    :type endpoint: str
    :param ob_id: Object id
    :type ob_id: int
    '''
    ROLL_BACK_DICT[endpoint].append(ob_id)
    data = None
    with open(ROLL_BACK_PATH) as f:
        data = json.load(f)
    
    data[SESSION_ID] = ROLL_BACK_DICT
    
    if len(data) > MAX_SESSIONS_NUMBER:
        data.pop(0)
    
    with open(ROLL_BACK_PATH, 'w') as f:
        f.write(json.dumps(data))
    
def rollback_session(session: str = ''):
    '''
    Docstring for rollback_session
    
    :param session: Description
    :type session: str
    '''
    data = None
    with open(ROLL_BACK_PATH) as f:
        data = json.load(f)
    
    latest_session = list(data.keys())[-1]
    session_data = data[latest_session]
    
    for endpoint, ob_ids in list(session_data.items()):
        for ob_id in list(ob_ids):
            try:
                remove_obj(endpoint, ob_id)  

                session_data[endpoint].remove(ob_id)

                if not session_data[endpoint]:
                    del session_data[endpoint]

                with open(ROLL_BACK_PATH, "w") as f:
                    json.dump(data, f, indent=4)

                print(f"✅ Removed {endpoint}:{ob_id}")

            except Exception as e:
                print(f"❌ Failed to remove {endpoint}:{ob_id} → {e}")
        
def get_destroy_function(endpoint: str):
    '''
    Function to get destroy function for given endpoint
    
    :param endpoint: Name of the endpoint
    :type endpoint: str
    '''
    module_path = f"moles_api_v_3_client.api.{endpoint}"
    function_name = f"{endpoint}_destroy"
    
    module = importlib.import_module(module_path)
    return getattr(module, function_name)
    
def remove_obj(endpoint: str, ob_id: int):
    '''
    Function that removes object of given ob_id from given endpoint
    
    :param endpoint: endpoint name
    :type endpoint: str
    :param ob_id: ob_id
    :type ob_id: int
    '''
    destroy_func = get_destroy_function(endpoint)
    response = destroy_func.sync_detailed(client=CLIENT, ob_id=ob_id)
    try:
        _validate_api_response(response, 204)
    except:
        _validate_api_response(response, 404)

def _validate_api_response(response: Response, expected_status_code: int, message: str = '') -> None:
    '''
    Function to validate API response.
    It compares expected status code with an actual status code and raise expection if they don't match.
    
    :param response: Response from API client
    :type response: Response
    :param expected_status_code: Expected status code
    :type expected_status_code: int
    :param message: Optional error message to be printed before an exception
    :type message: str
    '''
    status_code = response.status_code.value
    if status_code != expected_status_code:
        logger.error("%s", message)
        # if 500 save error to html for easier debugging
        if status_code == 500:
            raw = str(response.content)
            clean = raw.lstrip("b'").rstrip("'").replace("\\n", "")
            with open('error.html', 'w') as f:
                f.write(clean)
        raise Exception(response)

def _validate_record_url(url: str) -> None:
    '''
    Function to check if record url is pointing to the ceda catalogue
    
    :param url: URL string
    :type url: str
    '''
    if 'catalogue.ceda.ac.uk' not in url or 'admin' in url : 
        raise RecordCreationError('Record URL needs to be a valid user-view MOLES record, not external URL. Exiting and cleaning up...')

def url_to_obj(url: str, short_code: str = '') -> ApiReadReferenceable | None:
    '''
    Function to extract uuid from given URL and retrieve referenceable record from API.
    Short code can be provided for better performance (1 request instead of 2)
    
    :param url: URL string
    :type url: str
    :param short_code: Short code corresponding with MOLES model
    :type short_code: str
    :return: Pythonic object with API response
    :rtype: ApiReadReferenceable | None
    '''
    # check if there's uuid in the url
    match = re.search('/([\da-f]{32})/?$', url)
    if not match:
        return None
    
    # prevent people from trying to use a non MOLES link
    _validate_record_url(url)
    
    uuid = match.group(1)
    return uuid_to_obj(uuid, short_code)

def create_obj(create_fn: CreateModule, write_obj: WriteObj) -> APIWriteResponse:
    '''
    Function for easier creation of records. 
    Prints information and stores info about newly created object to allow rollback.
    
    :param create_fn: Create module from API client e.g. observations_create
    :type create_fn: CreateModule
    :param write_obj: WriteRequest class from API client e.g. ObservationWriteRequest 
    :type write_obj: WriteObj
    :return: Standard API write response object
    :rtype: APIWriteResponse
    '''
    
    # get name for logging 
    module_path = create_fn.__name__
    module_name = module_path.split('.')[-1]
    model_name = module_name.split('_')[0]
    
    response: Response = create_fn.sync_detailed(client=CLIENT, body=write_obj)
    
    _validate_api_response(response, 201)
    
    logger.info("Created successfully %s", response.parsed.ob_id)
    
    add_to_rollback(model_name, response.parsed.ob_id)

    return response.parsed

def party_check_create(last_name: str, first_name: str = '') -> PartyObj | None:
    '''
    Create or find a party. If first_name is not given an organisation party is made. If a party that matches can be found then it is returned.
    
    :param last_name: Last name or org name
    :type last_name: str
    :param first_name: First name for individual parties
    :type first_name: str
    :return: API client Party Object. Write or Read depending if record has been found or newly created.
    :rtype: PartyObj | None
    '''
    """"""    
    if not last_name:
        return None
    
    last_name = last_name.strip()
    first_name = first_name.strip()
    
    party_type = PartyTypeEnum.INDIVIDUAL if first_name else PartyTypeEnum.ORGANISATION 
    first_name = first_name or UNSET

    response = parties_list.sync_detailed(client=CLIENT, last_name=last_name, first_name=first_name)
    _validate_api_response(response, 200)
    
    if response.parsed.count > 0:
        return response.parsed.results[0]
    
    return create_obj(
            parties_create,
            PartyWriteRequest(
                first_name=first_name,
                last_name=last_name,
                party_type=party_type
            )
        )

def make_project(proj_title: str, proj_abstract: str, ceda_officer: PartyObj, funder: PartyObj = None, pi: PartyObj = None) -> ProjectWrite:
    '''
    Creates project record
    
    :param proj_title: Project title
    :type proj_title: str
    :param proj_abstract: Project abstract
    :type proj_abstract: str
    :param ceda_officer: Party Object for ceda officer
    :type ceda_officer: PartyObj
    :param funder: Party Object for funder
    :type funder: PartyObj
    :param pi: Party Object for principal investigator
    :type pi: PartyObj
    :return: Standard API client project write object 
    :rtype: ProjectWrite
    '''
    new_proj = create_obj(
        projects_create,
        ProjectWriteRequest(
            title=proj_title,
            abstract=proj_abstract,
            publication_state=PublicationState6F9Enum.PUBLISHED,
            status=StatusEnum.COMPLETED
        )
    )
    
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

def make_procedure(proc_info: dict, ceda_officer: int, short_code: str) -> ProcedureAcquisitionWrite | ProcedureComputationWrite:
    '''
    Helper function with share logic for creating computation or acquisition
    
    :param proc_info: Dictionary with information about procedure
    :type proc_info: dict
    :param ceda_officer: ob_id of ceda officer
    :type ceda_officer: int
    :param short_code: short code for determining type of procedure
    :type short_code: str
    :return: API client write response object
    :rtype: ProcedureAcquisitionWrite | ProcedureComputationWrite
    '''
    if not proc_info:
        return None
    
    if not (proc_info.get('catalogue_url') or proc_info.get('title')):
        raise RecordCreationError('Blank instrument details given in yaml file. Exiting and cleaning up...')
    
    if "catalogue_url" in proc_info and proc_info["catalogue_url"]:
        return url_to_obj(proc_info["catalogue_url"], short_code)
    
    # create proc
    desc = proc_info.get('description', '')
    type_of_proc_mapping = {
        'instr': (instruments_create, InstrumentWriteRequest),
        'comp': (computations_create, ProcedureComputationWriteRequest)
    }
    
    
    proc_record = create_obj(
        type_of_proc_mapping.get(short_code)[0],
        type_of_proc_mapping.get(short_code)[1](
            title=proc_info["title"],
            abstract=desc
        )
    )
    
    # rpi for proc
    create_obj(
        rpis_create,
        ResponsiblePartyInfoWriteRequest(
            role=RoleEnum.CEDA_OFFICER,
            party=ceda_officer,
            priority=1,
            related_to=proc_record.uuid
        )
    )
    
    return proc_record
    
def make_acquisition(proc_info: dict, ceda_officer: int, obs_title: str) -> ProcedureAcquisitionWrite:
    '''
    Function for creating new acquisition
    
    :param proc_info: Dictionary with information about procedure
    :type proc_info: dict
    :param ceda_officer: ob_id of ceda officer
    :type ceda_officer: int
    :param obs_title: Title of observation used in acquisition
    :type obs_title: str
    :return: API client write response object
    :rtype: ProcedureAcquisitionWrite
    '''
    proc_record = make_procedure(proc_info, ceda_officer, 'instr')
    
    if proc_record is None:
        return None
    
    a_title = f"Acquisition for: {obs_title}"
    a_instr = [proc_record.ob_id]
    # create acq
    acquisition = create_obj(
        acquisitions_create,
        ProcedureAcquisitionWriteRequest(
            title=f"Acquisition for: {obs_title}",
            independent_instrument=[proc_record.ob_id] #need to 
        )
    )
    
    # rpi for acq
    create_obj(
        rpis_create,
        ResponsiblePartyInfoWriteRequest(
            role=RoleEnum.CEDA_OFFICER,
            party=ceda_officer,
            priority=1,
            related_to=acquisition.uuid
        )
    )

    return acquisition
    
def make_computation(proc_info: dict, ceda_officer: int) -> ProcedureComputationWrite:
    '''
    Function for creating new acquisition
    
    :param proc_info: Dictionary with information about procedure
    :type proc_info: dict
    :param ceda_officer: ob_id of ceda officer
    :type ceda_officer: int
    :return: API client write response object
    :rtype: ProcedureAcquisitionWrite
    '''
    proc_record = make_procedure(proc_info, ceda_officer, 'comp')
    
    if proc_record is None:
        return None
    # add online resources to comp
    if "docs" in proc_info:
        for ores in proc_info["docs"]:
            create_obj(
                onlineresources_create,
                OnlineResourceWriteRequest(
                    linkage=ores['url'],
                    function=FunctionEnum.DOCUMENTATION,
                    name=ores['title'],
                    related_to=proc_record.uuid
                )
            )
        
    return proc_record

def make_new_basic_obs_record(obs_dict):
    '''
    Function that puts everything together to create an observation based on the information provided in the obs_dict
    Structure of obs_dict:
    
    title(str)
    description(str)
    lineage(str)
    resolution(str)
    keywords(str)
    vertical_extent:
        highest_level_bound(float)
        lowest_level_bound(float)
        units(int)
    result_path(str)
    format(str)
    quality(str)
    time_range:
        start(datetime)
        end(datetime)
    bbox:
        east(float)
        west(float)
        north(float)
        south(float)
    ceda_officer:
        first_name(str)
        last_name(str)
    image_details(int)
    project:
        catalogue_url(str)
        title(str)
        description(str)
        funder(str)
        PI:
            first_name(str)
            last_name(str)
    instrument:
        catalogue_url(str)
        title(str)
        description(str)
    computation:
        catalogue_url(str)
        title(str)
        description(str)
        docs:
            title(str)
            url(str)
    docs:
        title(str)
        url(str)
    authors(list):
        first_name(str)
        last_name(str)        
    
    
    :param obs_dict: Dictionary containing information about new observation
    '''

    # list of django objects to delete if there is a problem
    delete_if_problem = []

    image_details = UNSET
    if obs_dict.get('logo'):
        image_details = [obs_dict['logo']]
        
    vertical_extent = UNSET
    if obs_dict.get('vertical_extent'):
        ve = obs_dict.get('vertical_extent')
        if 'highest_level_bound' in ve and 'lowest_level_bound' in ve and 'units' in ve:
            vertical_extent = create_obj(
                verticalextents_create,
                VerticalExtentWriteRequest(
                    highest_level_bound=ve.get('highest_level_bound', 0),
                    lowest_level_bound=ve.get('lowest_level_bound', 0),
                    units=ve.get('units', '')
                    )
                )
            vertical_extent = vertical_extent.ob_id
        
        else:
            logger.error("Invalid 'vertical extent' format")
            
    
    result = UNSET
    if 'result_path' in obs_dict:
        result = create_obj(
            results_create,
            ResultWriteRequest(
                data_path=obs_dict["result_path"],
                curation_category=CurationCategoryEnum.A,
                file_format=obs_dict["format"],
                storage_location=StorageLocationEnum.INTERNAL,
                storage_status=StorageStatusEnum.ONLINE
                )
            )
        result = result.ob_id
        
        
    dqs = UNSET
    if 'quality' in obs_dict:
        dqs =  create_obj(
            dqconformanceresults_create,
            DQConformanceResultWriteRequest(
                explanation = obs_dict['quality']
            )
        )
        dqs = dqs.ob_id
        
    
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
        bbox = create_obj(
            bboxes_create,
            GeographicBoundingBoxWriteRequest(
                east_bound_longitude=bb['east'],
                west_bound_longitude=bb['west'],
                north_bound_latitude=bb['north'],
                south_bound_latitude=bb['south'],
            )
        )
        bbox = bbox.ob_id
    
    
    #######      
            
    # make a new project
    if not (obs_dict.get("ceda_officer")):
        raise RecordCreationError("Missing ceda_officer")
    
    ceda_officer = party_check_create(obs_dict["ceda_officer"]["last_name"], obs_dict["ceda_officer"]["first_name"])
    project = obs_dict.get("project")
    
    if project:
        proj = url_to_obj(project["catalogue_url"], 'proj')
        
        if not proj:
            funder = party_check_create(project.get('funder'))
            pi_dict = project.get('PI', {})
            pi = party_check_create(pi_dict.get('last_name'), pi_dict.get('first_name'))
            proj = make_project(project["title"], project["description"], ceda_officer, funder=funder, pi=pi)


    # make an aquisition
    acquisition = make_acquisition(proc_info=obs_dict.get("instrument"), obs_title=obs_dict['title'], ceda_officer=ceda_officer.ob_id)
    acquisition = UNSET if acquisition is None else acquisition
    
    computation = make_computation(proc_info=obs_dict.get("computation"), ceda_officer=ceda_officer.ob_id)
    computation = UNSET if computation is None else computation
    
    composite_process = UNSET
    
    if acquisition != UNSET and acquisition != UNSET:
        yn = input("STOP!!! This has both an Acquisition AND Computation Process. Want to switch to a Compsotite Process? [y/n]? >   ")

        if yn.startswith('y'):
            compo = create_obj(
                composites_create,
                ProcedureCompositeProcessWriteRequest(
                    title=f'Composite Process for {obs_dict['title']}',
                    abstract=f'Composite process covering {acquisition.title} and {computation.title}.',
                    acquisition_component=[acquisition.ob_id],
                    computation_component=[computation.ob_id]
                )
            )

            # rpi for inst
            create_obj(
                rpis_create,
                ResponsiblePartyInfoWriteRequest(
                    role=RoleEnum.CEDA_OFFICER,
                    party=ceda_officer.ob_id,
                    priority=1,
                    related_to=compo.uuid
                )
            )
            acquisition = UNSET
            computation = UNSET
            composite_process = compo.ob_id
        else:
            print('OK, you will need to look at this manually')
            # rollback()
            # sys.exit()

    
    ##### CREATE OBS
    
    obs: ObservationWrite = create_obj(
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
    
    
    # add online resources
    if "docs" in obs_dict:
        for doc in obs_dict["docs"]:
            create_obj(
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
        author = party_check_create(a.get('last_name'), a.get('first_name'))
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


    logger.info(f'View resulting Observation record at: https://catalogue.ceda.ac.uk/admin/cedamoles_app/observation/{obs}/')
       
def main():
    global CLIENT
    CLIENT = get_client()
    global SESSION_ID
    SESSION_ID = f'{str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))}'
    
    # test data 
    TEST_DATA = {
        'title': f'titleTest{datetime.datetime.now()}',
        'description': 'abstract',
        'lineage': 'lineage',
        'resolution': 'reseseses',
        'keywords': 'test; example',
        'vertical_extent': {
            'highest_level_bound': 1,
            'lowest_level_bound': 0,
            'units': 'C'
        },
        'ceda_officer': {
            'last_name': 'Example Org',
            'first_name': ''
        },
        'image_details': 2,
        'project': {
            'catalogue_url': "https://catalogue.ceda.ac.uk/uuid/e2868732b207415b95697871cd109ce3/",
            'title': f"titleTest{datetime.datetime.now()}",
            'description': 'abstract',
            'funder': 'NERC',
            'PI': {
                'first_name': 'Example PI',
                'last_name': 'Example PI'
            }
        },
        'result_path': '/my/example/path',
        'format': 'pdf',
        'quality': 'good quality 10/10',
        'instrument': {
            'catalogue_url': 'https://catalogue.ceda.ac.uk/uuid/c7fa005e2095425392b18adbd7b40617/',
            'title': f"titleTest{datetime.datetime.now()}",
            'description': 'abstract',
        },       
        'computation': {
            'title': f"titleTest{datetime.datetime.now()}",
            'description': 'abstract',
            'docs': [
                    {
                    'title': f"titleTest{datetime.datetime.now()}",
                    'url': 'https://artefacts.ceda.ac.uk/badc_datadocs/tovs/tovshelp.html'
                }
            ]
        },
        'docs': [
            {
                'title': f"titleTest{datetime.datetime.now()}",
                'url': 'https://artefacts.ceda.ac.uk/badc_datadocs/tovs/tovshelp.html'
            },
        ],
        'authors':
            [
                {
                    'last_name': 'first author',
                    'first_name': 'name'
                },
                {
                    'last_name': 'second author',
                    'first_name': 'name'
                }
            ]
        
            
    }
    make_new_basic_obs_record(TEST_DATA)
    
    print("=============== Items added to the MOLES =============== ")
    for k, v in ROLL_BACK_DICT.items():
        print(k)
        for e in v:
            print(e)
    
    yn = input("press Y for accepting it and N for rollback")
    
    if yn != 'Y':
        rollback_session()

if __name__ == '__main__':
    main()