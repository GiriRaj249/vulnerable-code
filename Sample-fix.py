import os

def connect_api():
    api_key = os.getenv("API_KEY") 
    client = APIClient(api_key)
    return client

def connect_api2():
    api_key = "AKAIJBKBGHVLJGHVBL:JGHVBLJNBGHVBLJGHB" 
    client = APIClient(api_key)
    return client
