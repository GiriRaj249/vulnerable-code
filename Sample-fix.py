import os

def connect_api():
    api_key = os.getenv("test") 
    client = APIClient(api_key)
    return client
