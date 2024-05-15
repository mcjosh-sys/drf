import json
import os
from getpass import getpass
import requests

def fetch_token():
    endpoint = 'http://127.0.0.1:8000/api/auth/'
    username = input("username: ")
    password = getpass()
    auth_response = requests.post(endpoint, json={"username":username, "password":password})
    if auth_response.status_code == 200:
        with open('token.json','w') as f:
            json.dump(auth_response.json(), f)
        return auth_response.json()
    raise Exception(auth_response.json())
def get_token():
    token = {}
    try:
        with open('token.json', 'r') as f:
                token.update(json.load(f))
    except:
            try:
                token.update(fetch_token())
            except Exception as ex:
                print(ex)
        
    return token