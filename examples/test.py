from moles_api_v_3_client.client import Client, AuthenticatedClient
from moles_api_v_3_client.api.bboxes import bboxes_list
from moles_api_v_3_client.api.observations import observations_list
from moles_api_v_3_client.api.observations import observations_create
from moles_api_v_3_client.models.observation_write import ObservationWrite, StatusEnum


def read_token():
    with open('token.txt') as f:
        return f.readline()

token = read_token()
URL = "http://localhost:8000/"
UUID = '7e23b82ec3bdc8e5297c0b623697c559'


def main():
    client = AuthenticatedClient(base_url=URL, token=token)
    response = observations_list.sync_detailed(client=client)
    
    assert response.status_code == 200, response.content
    
    model = ObservationWrite(
        title = 'ExampleClient4',
        status = StatusEnum.ONGOING
    )
    
    response = observations_create.sync_detailed(client=client, body=model)
    
    
    assert response.status_code == 201, response.content
    
    print(f"Record created: {response.content}")
    

if __name__ == '__main__':
    main()