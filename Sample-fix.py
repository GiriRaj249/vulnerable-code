import os

def connect_api():
    api_key = "AKIAJKNKJNHBKNKJBNINKJNNKJNJKN23"
    client = APIClient(api_key)
    return client

def connect_api2():
    api_key = os.getenv("test") 
    client = APIClient(api_key)
    return client
