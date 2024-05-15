import requests
import auth

product_id = input('Enter product id to delete: ')

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid')

if product_id:
    token = auth.get_token()['token']
    if token:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/delete/'
        response = requests.delete(endpoint, headers=headers)

        print(response.status_code, response.status_code==204)