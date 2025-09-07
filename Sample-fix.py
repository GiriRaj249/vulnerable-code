import os

def connect_api():
    api_key = os.getenv("API_KEY") 
    client = APIClient(api_key)
    return client


yterst

def connect_api2():
    api_key = os.getenv("test") 
    client = APIClient(api_key)
    return client
