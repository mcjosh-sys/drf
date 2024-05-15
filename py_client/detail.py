import requests
import auth

produt_id = input("Product Id: ")
try:
    product_id = int(produt_id)
except Exception as e:
    product_id = None
    print(e)
if product_id:
    token = auth.get_token()['token']
    if token:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/'

        response = requests.get(endpoint, headers=headers)

        print(response.json())