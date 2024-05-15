import requests
import auth
import utils

data = {}
print("Enter product details")
print("======================")
product_id = utils.collect_data(data, 'update')

token = auth.get_token()['token']
if token:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/update/'

    response = requests.patch(endpoint, json=data, headers=headers)

    print(response.json())