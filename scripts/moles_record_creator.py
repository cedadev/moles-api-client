from scripts.imports.api import *
from scripts.imports.models import *
from scripts.imports.typing_moles import *
from scripts.utils import *
from scripts.moles_basic_tools import uuid_to_obj, ApiReadReferenceable, _get_value_enum

from moles_api_v_3_client.types import Response, UNSET
import datetime, re, logging, importlib, json, yaml
from collections import defaultdict

FILES_PATH = Path(__file__).resolve().parent / 'files' 
SESSIONS_DICT = defaultdict(list)
MAX_SESSIONS_NUMBER = 20

VALID_INPUT_TYPES = [
    'yml',
    'json',
    'text'
]

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

TEST_OBSERVATION = {
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
        'result_path': '/my/example/path',
        'format': 'pdf',
        'quality': 'good quality 10/10',
        'timerange':
            {
                'start': '1978-12-01T00:00:00Z',
                'end': '1998-06-29T23:00:00Z'
            },
        'bbox': {
            'east': 10,
            'west': -10,
            'north': 10,
            'south': -10
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

TEST_PROJECT = {
    'title': f'titleTest{datetime.datetime.now()}',
    'description': 'abstract',
    'ceda_officer': {
            'last_name': 'Example Org',
            'first_name': ''
        },
    'funder': 'NERC',
    'PI': {
        'first_name': 'Example PI',
        'last_name': 'Example PI'
    }
    
}

def add_to_sessions(endpoint: str, ob_id: int):
    '''
    Function to add endpoint and ob_id to the rollback file under current session
    
    :param endpoint: Endpoint name
    :type endpoint: str
    :param ob_id: Object id
    :type ob_id: int
    '''
    SESSIONS_DICT[endpoint].append(ob_id)
    data = get_sessions_dict()
    
    data[SESSION_ID] = SESSIONS_DICT
    
    if len(data) > MAX_SESSIONS_NUMBER:
        data.pop(0)
    
    save_sessions_dict(data)

def get_destroy_function(endpoint: str):
    '''
    Function to get destroy function for given endpoint
    
    :param endpoint: Endpoint name
    :type endpoint: str
    '''
    module_path = f"moles_api_v_3_client.api.{endpoint}"
    function_name = f"{endpoint}_destroy"
    
    module = importlib.import_module(module_path)
    return getattr(module, function_name)
    
def remove_obj(endpoint: str, ob_id: int):
    '''
    Function that removes object of given ob_id from given endpoint
    
    :param endpoint: Endpoint name
    :type endpoint: str
    :param ob_id: ob_id
    :type ob_id: int
    '''
    destroy_func = get_destroy_function(endpoint)
    response = destroy_func.sync_detailed(client=CLIENT, ob_id=ob_id)
    try:
        validate_api_response(response, 204)
    except:
        validate_api_response(response, 404)
    
def rollback_session(session: str = ''):
    '''
    Function to remove all records created in given session
    
    :param session: Session id; if empty latest session is taken
    :type session: str
    '''
    data = get_sessions_dict()
    
    if not session:
        session = list(data.keys())[-1]
    session_data = data[session]
    
    for endpoint, ob_ids in list(session_data.items()):
        for ob_id in list(ob_ids):
            try:
                remove_obj(endpoint, ob_id)  
                session_data[endpoint].remove(ob_id)
                save_sessions_dict(data)
                print(f"✅ Removed {endpoint}:{ob_id}")
                
            except Exception as e:
                print(f"❌ Failed to remove {endpoint}:{ob_id} → {e}")
                
        if not session_data[endpoint]:
            del session_data[endpoint]
            
    if not data[session]:
        del data[session]
                    
    save_sessions_dict(data)

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
    match = re.search(r'/([\da-f]{32})/?$', url)
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
    
    validate_api_response(response, 201)
    
    logger.debug("Created successfully %s", response.parsed.ob_id)
    
    add_to_sessions(model_name, response.parsed.ob_id)

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
    validate_api_response(response, 200)
    
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

def make_project(proj_dict: dict) -> ProjectWrite:
    '''
    Creates project record 
    Proj_dict structure:
    
    title(str)
    description(str)
    ceda_officer:
        last_name(str)
        first_name(str)
    PI:
        last_name(str)
        first_name(str)
    funder(str)
    '''
    title=proj_dict.get('title'),
    abstract=proj_dict.get('description'),
    new_proj = create_obj(
        projects_create,
        ProjectWriteRequest(
            title=proj_dict.get('title'),
            abstract=proj_dict.get('description'),
            publication_state=PublicationState6F9Enum.PUBLISHED,
            status=StatusEnum.COMPLETED
        )
    )
    co_fn, co_ln = None, None
    ceda_officer = proj_dict.get('ceda_officer')
    if ceda_officer:
        co_fn = ceda_officer.get('first_name')
        co_ln = ceda_officer.get('last_name')
    
    pi_fn, pi_ln = None, None
    pi = proj_dict.get('PI')
    if pi:
        pi_fn = pi.get('first_name')
        pi_ln = pi.get('last_name')
    
    funder = proj_dict.get('funder')
    
    rpis_to_create = [
        ('ceda_officer', party_check_create(co_ln, co_fn)),
        ('funder', party_check_create(funder)),
        ('principal_investigator', party_check_create(pi_ln, pi_fn))
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
            project['ceda_officer'] = obs_dict.get('ceda_officer')
            proj = make_project(project)


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
            procedure_composite_process = composite_process,
            non_geographic_flag=(bbox is UNSET),
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


    return obs
       
def choose_session() -> str | None:
    '''
    Function that allows choosing session without typiong exact id
    
    :return: session id
    :rtype: str | None
    '''
    
    print(10 * '=' + "Choose session to rollback" + 10 * '=')
    data = get_sessions_dict()
    sessions = list(data.keys())
    n = 0
    for session, endpoints in data.items():
        n += 1
        count = 0
        for _, v in endpoints.items():
            count += len(v)
            
        print(f'{n}. {session}: {count} records')
    print(f'{n + 1}. Exit')
    
    choice = input('Choice: ')
    choice = int(choice) - 1
    if 0 <= choice < len(sessions):
        return sessions[choice]
    
    if choice != len(sessions):
        print_invalid_choice()
        
    return None

def print_invalid_choice():
    print("Invalid option. Please try again.")

def print_main_menu() -> None:
    '''
    Shortcut for printing main menu
    '''
    print("\n=== MAIN MENU ===")
    print("1. Add observation")
    print("2. Add project")
    print("3. Test obs upload")
    print("4. Print current session")
    print("5. Rollback")
    print("6. Exit")

def print_current_session() -> None:
    '''
    Print all records created in the current session
    '''
    sessions = get_sessions_dict()
    s = sessions.get(SESSION_ID)
    if not s:
        return
    
    print(10 * '=' + 'Current session' + 10 * '=')
    for endpoint, ids in s.items():
        print(endpoint)
        for ob_id in ids:
            print(f'\t{ob_id}')

def input_to_dict(input_type: str, data: str) -> dict:
    '''
    Docstring for input_to_dict
    
    :param input_type: yml, json or text
    :type input_type: str
    :param data: filepath or data
    :type data: str
    :return: moles record dict
    :rtype: dict
    '''
    
    if input_type not in VALID_INPUT_TYPES:
        return None
    
    if input_type == 'text':
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            print(e)
            return None
    
    raw_string = None
    try:
        with open(FILES_PATH / data) as f:
            raw_string = f.read()
    except FileNotFoundError:
        print("File not found!")
        return None
    
    if input_type == 'yml':
        return yaml.safe_load(raw_string)
    return json.loads(raw_string)

def user_input_data() -> tuple:
    '''
    Function to get user input for record creation
    
    :return: Type of input (e.g. yml, text) and filepath/string
    :rtype: tuple
    '''
    print('Available input types:')
    print(";".join(VALID_INPUT_TYPES))
    
    input_type = input('Choose input type: ')
    data = input('Provide filename for json/yml, or serialized json string if you chose "text": ')
    
    return (input_type, data)

def main_menu():
    '''
    Function that hanles main menu loop 
    '''
    while True:
        print_main_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            input_type, record_dict = user_input_data()
            record_dict = input_to_dict(input_type, record_dict)
            
            if record_dict is None:
                print_invalid_choice()
            else:
                make_new_basic_obs_record(record_dict)
            
        elif choice == "2":
            input_type, record_dict = user_input_data()
            record_dict = input_to_dict(input_type, record_dict)
            
            if record_dict is None:
                print_invalid_choice()
            else:
                make_project(record_dict)

        elif choice == "3":
            make_new_basic_obs_record(TEST_OBSERVATION)
            
        elif choice == "4":
            print_current_session()
            
        elif choice == "5":
            choice = choose_session()
            if choice is not None:
                rollback_session(choice)
                
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
            
def main():
    global CLIENT
    CLIENT = get_client()
    global SESSION_ID
    SESSION_ID = f'{str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))}'
    
    main_menu()

if __name__ == '__main__':
    main()