import requests
from getpass import getpass
import auth


# endpoint = 'http://127.0.0.1:8000/api/auth/'
# username = input("username: ")
# password = getpass()

# auth_response = requests.post(endpoint, json={"username":username, "password":password})

# print(auth_response.json())

token = auth.get_token()['token']
if token:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = 'http://127.0.0.1:8000/api/products/'
    response = requests.get(endpoint, headers=headers)

    print(response.json())