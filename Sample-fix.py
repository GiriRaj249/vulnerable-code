import os

def connect_api():
    api_key = os.getenv("API_KEY") 
    client = APIClient(api_key)
    return client

def nothing():
    print("no changes in monitored code")
    
def name():
    user_id = 42
    id = cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return id
    
def connect_api2():
    api_key = os.getenv("test") 
    client = APIClient(api_key)
    return client
