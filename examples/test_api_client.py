from moles_api_v_3_client.client import AuthenticatedClient

from moles_api_v_3_client.api.projects import projects_create
from moles_api_v_3_client.api.results import results_create
from moles_api_v_3_client.api.observations import observations_create

from moles_api_v_3_client.models import (
    ProjectWriteRequest,
    ResultWriteRequest,
    ObservationWriteRequest,
    StatusEnum,
)



import time
import datetime
from random import randint

BASE_URL = "http://localhost:8000/"

def read_token():
    with open('token.txt') as f:
        return f.readline()
    
def create_n_record(n, proj_title, obs_title, res_path):
    def response_validation(response, name='Object'):
        if response.status_code.value != 201:
            raise Exception(f"{name} hasn't been created. {response.content}")
        
    token = read_token()
    client = AuthenticatedClient(base_url=BASE_URL, token=token)
    
    
    proj = ProjectWriteRequest(
        title=proj_title, abstract='Example',
    )
    proj_response = projects_create.sync_detailed(client=client, body=proj)
    response_validation(proj_response, 'Project')
    
    proj_id = proj_response.parsed.ob_id
    
    for i in range(n):
        res = ResultWriteRequest(
            data_path=f'{res_path}{i}',
        )
        result_response = results_create.sync_detailed(client=client, body=res)
        response_validation(result_response, 'Result')
        
        result_id = result_response.parsed.ob_id
        
        obs = ObservationWriteRequest(
            status=StatusEnum.ONGOING, 
            title=f'{obs_title}{i}',
            abstract="Example Abstract",
            result_field=result_id,
            projects=[proj_id]
            
        )
        obs_response = observations_create.sync_detailed(client=client, body=obs)
        response_validation(obs_response, 'Observation')
        

def main():
    r_int = randint(1, 10000)
    
    start = time.time()
    
    create_n_record(50, f'ProjectC{r_int}', f'ObsC{r_int}', f'/obs/client/path{r_int}')
    
    end = time.time()
    
    print(datetime.timedelta(seconds=end - start))
    
    
    

if __name__ == '__main__':
    main()