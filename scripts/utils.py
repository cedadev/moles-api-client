from moles_api_v_3_client.client import Client, AuthenticatedClient
from moles_api_v_3_client.types import Response
from scripts.imports.typing_moles import RecordCreationError

import os, json, logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

SESSIONS_PATH = Path(__file__).resolve().parent / 'files' / 'sessions.json'

def get_client():
    token = os.environ.get("API_TOKEN")
    base_url = os.environ.get("API_URL")
    if not base_url:
        print("MISSING URL!!! Set base url with `export API_URL=http://example.com`")
        exit(1)
        
    if not token:
        print("MISSING API TOKEN! Writing is not available without it. Set it with `API_TOKEN=token`")
    if token:
        return AuthenticatedClient(base_url=base_url, token=token, verify_ssl=False)
    return Client(base_url=base_url)

def get_sessions_dict() -> dict:
    data = None
    with open(SESSIONS_PATH) as f:
        data = json.load(f)
        
    return data
    
def save_sessions_dict(data: dict):
    with open(SESSIONS_PATH, 'w') as f:
        json.dump(data, f, indent=4)   
        

def validate_api_response(response: Response, expected_status_code: int, message: str = '') -> None:
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
    
def validate_record_url(url: str) -> None:
    '''
    Function to check if record url is pointing to the ceda catalogue
    
    :param url: URL string
    :type url: str
    '''
    if 'catalogue.ceda.ac.uk' not in url or 'admin' in url : 
        raise RecordCreationError('Record URL needs to be a valid user-view MOLES record, not external URL. Exiting and cleaning up...')

