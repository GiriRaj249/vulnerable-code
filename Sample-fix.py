import os

def connect_api():
    api_key = os.getenv("API_KEY") 
    client = APIClient(api_key)
    return client
    
def name():
    user_id = input("Enter input: ")
    id = cursor.execute(f"SELECT * FROM users WHERE id = {user_id}"
    return id
    
def connect_api2():
    api_key = os.getenv("test") 
    client = APIClient(api_key)
    return client
