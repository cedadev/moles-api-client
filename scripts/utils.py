import os
from moles_api_v_3_client.client import Client, AuthenticatedClient

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