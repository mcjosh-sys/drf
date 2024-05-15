import requests

endpoint = 'http://127.0.0.1:8000/api/products/1123455/'

response = requests.get(endpoint)

print(response.json())