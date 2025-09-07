import os

def connect_api():
    api_key = os.getenv("API_KEY") 
    client = APIClient(api_key)
    return client
