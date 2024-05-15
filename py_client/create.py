import requests
import auth
import utils

data = {}
print("Enter product details")
print("======================")
utils.collect_data(data)

token = auth.get_token()['token']
if token:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = f'http://127.0.0.1:8000/api/products/'

    response = requests.post(endpoint, json=data, headers=headers)

    print(response.json())