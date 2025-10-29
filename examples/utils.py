import os
from moles_api_v_3_client.client import Client, AuthenticatedClient

def get_client():
    token = os.environ.get("API_TOKEN")
    base_url = os.environ.get("API_URL")
    if token:
        return AuthenticatedClient(base_url=base_url, token=token)
    return Client(base_url=base_url)