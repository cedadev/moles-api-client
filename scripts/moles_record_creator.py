
from moles_api_v_3_client.api.observations import observations_create, observations_partial_update, observations_update
from moles_api_v_3_client.models.observation_write_request import ObservationWriteRequest, StatusEnum, PublicationStateCbbEnum, UpdateFrequencyEnum

from moles_api_v_3_client.api.results import results_create
from moles_api_v_3_client.models.result_write_request import ResultWriteRequest, CurationCategoryEnum, StorageLocationEnum, StorageStatusEnum

from moles_api_v_3_client.api.verticalextents import verticalextents_create
from moles_api_v_3_client.models.vertical_extent_write_request import VerticalExtentWriteRequest

from moles_api_v_3_client.api.imagedetails import imagedetails_list

from moles_api_v_3_client.api.dqconformanceresults import dqconformanceresults_create
from moles_api_v_3_client.models.dq_conformance_result_write_request import DQConformanceResultWriteRequest

from moles_api_v_3_client.api.times 
from moles_api_v_3_client.models.time_period_request import TimePeriodRequest

from moles_api_v_3_client.types import Response, UNSET
from scripts.utils import get_client
import datetime
import sys


ROLL_BACK_LIST = []

def _validate_api_response(response: Response, expected_status_code: int, message: str = '') -> None:
    status_code = response.status_code.value
    if status_code != expected_status_code:
        print(message)
        raise Exception(response)
    

def _get_model_ops(model: str):
    """
    Dynamically resolve *_create, *_update, *_list, *_destroy, and
    <Model>WriteRequest classes from the module's namespace.
    """
    
    current_module = sys.modules[__name__]
    namespace = current_module.__dict__
    
    create_fn = namespace.get(f"{model.lower()}s_create")
    update_fn = namespace.get(f"{model.lower()}s_update")
    list_fn   = namespace.get(f"{model.lower()}s_list")
    destroy_fn = namespace.get(f"{model.lower()}s_destroy")
    
    
    class_name = "".join([model, "WriteRequest"])
    write_cls = namespace.get(class_name)
    
    if not write_cls:
        class_name = "".join([model, "Request"])
        write_cls = namespace.get(class_name)
        
    
    if not any([create_fn, update_fn, list_fn, destroy_fn, write_cls]):
        raise ValueError(f"No matching API/model definitions found for '{model}'")
    
    return {
        "create": create_fn,
        "update": update_fn,
        "list": list_fn,
        "destroy": destroy_fn,
        "write_cls": write_cls,
    }

def create_obj(model_name: str, **kwargs) -> Response:
    """function to make a moles object """
    
    print(f'Creating {model_name} object')
    model_ops = _get_model_ops(model_name)
    
    create_fn = model_ops.get('create')
    write_cls = model_ops.get('write_cls')
    
    print(kwargs)
    
    model = write_cls(
        **kwargs
    )
    response: Response = create_fn.sync_detailed(client=CLIENT, body=model)
    
    _validate_api_response(response, 201)
    
    print(f"Created succesfully {response.parsed.ob_id}")
    
    ROLL_BACK_LIST.append((model_name, response.parsed.ob_id))

    return response


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
                'VerticalExtent', 
                highest_level_bound=ve.get('highest_level_bound', 0),
                lowest_level_bound=ve.get('lowest_level_bound', 0),
                units=ve.get('units', '')
                )
            vertical_extent = response.parsed.ob_id
        
        else:
            print("Invalid 'vertical extent' format")
            
    
    result = UNSET
    if 'result_path' in obs_dict:
        response = create_obj(
            'Result', 
            data_path=obs_dict["result_path"],
            curation_category=CurationCategoryEnum.A,
            file_format=obs_dict["format"],
            storage_location=StorageLocationEnum.INTERNAL,
            storage_status=StorageStatusEnum.ONLINE
            )
        result = response.parsed.ob_id
        
        
    dqs = UNSET
    if 'quality' in obs_dict:
        response =  create_obj(
            'DQConformanceResult',
            explanation = obs_dict['quality']
        )
        dqs = response.parsed.ob_id
        
        
    # make time range object
    timerange = create_obj(TimePeriod, startTime=obs_dict["time_range"]["start"], endTime=obs_dict["time_range"]["end"])
    ob.timePeriod = timerange
    
    
    timerange = UNSET
    if 'time_range' in obs_dict:
        tr = obs_dict['time_range']
        if 'start' in tr and 'end' in tr:
            response = create_obj('TimePeriod')
    
    
    
    
    create_obj(
        'Observation',
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
        result=result,
        result_quality=dqs
    )
    
    return
    
    ObservationWriteRequest(
        'Observation',
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
        result=result,
        result_quality=dqs
    )
    
    return
    
    
    

    

    

    # make a geo extent 
    bbox = obs_dict["bbox"]
    geo = create_obj(GeographicBoundingBox, eastBoundLongitude=float(bbox["east"]), westBoundLongitude=float(bbox["west"]),
                                northBoundLatitude=float(bbox["north"]), southBoundLatitude=float(bbox["south"]))
    ob.geographicExtent = geo
    ob.save()

    # make a new project
    ceda_officer = party_check_create(obs_dict["ceda_officer"]["surname"], obs_dict["ceda_officer"]["firstname"])
    project = obs_dict["project"]
 
    if "catalogue_url" in project and project["catalogue_url"]:
        if 'catalogue.ceda.ac.uk' not in project["catalogue_url"] or 'admin' in project["catalogue_url"] : #to prevent people from trying to use a non MOLES link
                raise RecordCreationError('Proejct record URL needs to be a valid user-view MOLES record, not external URL. Exiting and cleaning up...')

        proj = find_from_url(project["catalogue_url"], Project)
        
    else:
        if "funder" in project:
            funder = party_check_create(project["funder"])
        else:
            funder = None
        if "PI" in project:
            pi = party_check_create(project["PI"]["surname"], project["PI"]["firstname"])
        else:
            pi = None
        proj = make_project(project["title"], project["description"], ceda_officer, funder=funder, pi=pi)
    ob.projects.add(proj)

    # add parties to ob record
    create_obj(ResponsiblePartyInfo, role='ceda_officer', party=ceda_officer, priority=1, relatedTo=ob)
    # add authors
    i = 1

    for a in obs_dict["authors"]:
        if "firstname" in a: 
            author = party_check_create(a["surname"], a["firstname"])
        else: 
            author = party_check_create(a["surname"])
        create_obj(ResponsiblePartyInfo, role='author', party=author, priority=i, relatedTo=ob)
        i += 1

    ob.save()

    # add online resources
    if "docs" in obs_dict:
        for ores in obs_dict["docs"]:
            create_obj(OnlineResource, linkage=ores["url"], function="documentation", name=ores["title"], relatedTo=ob)

    # add instruments
    
    if "instrument" in obs_dict and obs_dict['instrument']:
        # make an aquisition

        inst_info = obs_dict["instrument"]
        if "catalogue_url" in inst_info and inst_info["catalogue_url"]:
            if 'catalogue.ceda.ac.uk' not in inst_info["catalogue_url"] or 'admin' in inst_info["catalogue_url"] : #to prevent people from trying to use a non MOLES link
                raise RecordCreationError('Instrument record URL needs to be a valid user-view MOLES record, not external URL. Exiting and cleaning up...')

            acquisition = create_obj(Acquisition, title="Acquisition for: "+obs_dict["title"])
            if not check_if_role_already_exists('ceda_officer', acquisition):
                create_obj(ResponsiblePartyInfo, role='ceda_officer', party=ceda_officer, priority=1, relatedTo=acquisition)

            ob.procedureAcquisition = acquisition
            ob.save() 
            
            inst = find_from_url(inst_info["catalogue_url"], Instrument)
            acquisition.independentInstrument.add(inst)
            
        elif "title" in inst_info and inst_info["title"]:
            acquisition = create_obj(Acquisition, title="Acquisition for: "+obs_dict["title"])
            create_obj(ResponsiblePartyInfo, role='ceda_officer', party=ceda_officer, priority=1, relatedTo=acquisition)
            ob.procedureAcquisition = acquisition
            ob.save() 
        
            if "description" in inst_info:
                desc = inst_info["description"]
            else:
                desc = ''
            
            inst = create_obj(Instrument, title=inst_info["title"], abstract=desc)
            create_obj(ResponsiblePartyInfo, role='ceda_officer', party=ceda_officer, priority=1, relatedTo=inst)
            acquisition.independentInstrument.add(inst)
            ob.save()         
            print(inst)
        else:
            raise RecordCreationError('Blank instrument details given in yaml file. Exiting and cleaning up...')
    # add computation
    if "computation" in obs_dict and obs_dict["computation"]:
        comp_info = obs_dict["computation"]
        if "catalogue_url" in comp_info and comp_info["catalogue_url"]:
            if 'catalogue.ceda.ac.uk' not in comp_info["catalogue_url"] or 'admin' in comp_info["catalogue_url"] : #to prevent people from trying to use a non MOLES link
                raise RecordCreationError('Computation record URL needs to be a valid user-view MOLES record, not external URL. Exiting and cleaning up...')

            comp = find_from_url(comp_info["catalogue_url"], Computation)
            if not check_if_role_already_exists('ceda_officer', comp):
                create_obj(ResponsiblePartyInfo, role='ceda_officer', party=ceda_officer, priority=1, relatedTo=comp)

        elif "title" in comp_info and comp_info['title']:
            if "description" in comp_info:
                desc = comp_info["description"]
            else:
                desc = ''
            comp = create_obj(Computation, title=comp_info["title"], abstract=desc)
            create_obj(ResponsiblePartyInfo, role='ceda_officer', party=ceda_officer, priority=1, relatedTo=comp)

        else:
            raise RecordCreationError('Blank computation details given in yaml file. Exiting and cleaning up...')
        if comp:
            ob.procedureComputation = comp
            ob.save()

        # add online resources to comp
        if "docs" in comp_info:
            for ores in comp_info["docs"]:
                create_obj(OnlineResource, linkage=ores["url"], function="documentation", name=ores["title"],
                           relatedTo=comp)

    if ob.procedureAcquisition and ob.procedureComputation:
        yn = input("STOP!!! This has both an Acquisition AND Computation Process. Want to switch to a Compsotite Process? [y/n]? >   ")

        if yn.startswith('y'):
            ob.procedureComputation = None
            ob.save()
            ob.procedureAcquisition = None
            ob.save()

            compo = create_obj(CompositeProcess, title=f'Composite Process for {ob.title}', abstract=f'Composite process covering {acquisition.title} and {comp.title}.')
            create_obj(ResponsiblePartyInfo, role='ceda_officer', party=ceda_officer, priority=1, relatedTo=compo)

            compo.acquisitionComponent.add(acquisition)
            compo.save()
            compo.computationComponent.add(comp)
            compo.save()
            ob.procedureCompositeProcess = compo
            ob.save()

        else:
            print('OK, you will need to look at this manually')
            rollback()
            sys.exit()

    print(f'View resulting Observation record at: https://catalogue.ceda.ac.uk/admin/cedamoles_app/observation/{ob.ob_id}/')

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
        }
    }
    make_new_basic_obs_record(obs_dict)

if __name__ == '__main__':
    main()