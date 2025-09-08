import os

def connect_api():
    api_key = os.getenv("API_KEY") 
    client = APIClient(api_key)
    return client
    
def name():
    user_id = input("Enter url: ")
    id = cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    #this change will result in SQLi since it pass user input in query directly
    return id
    
def connect_api2():
    api_key = os.getenv("test") 
    client = APIClient(api_key)
    return client
