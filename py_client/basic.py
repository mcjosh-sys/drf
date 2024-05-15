import requests
import json

endpoint = 'https://httpbin.org/status/200/'
endpoint = 'http://127.0.0.1:8000/api/'
endpoint = 'https://httpbin.org/anything'


data = {
  "args": {
    "abc": "123"
  },
  "data": "{\"title\": \"hello\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "18",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.31.0",
    "X-Amzn-Trace-Id": "Root=1-6638bd20-00f44b21310eff926a67398c"
  },
  "json": {
    "title": "hello"
  },
  "method": "POST",
  "origin": "102.89.46.92",
  "url": "https://httpbin.org/anything?abc=123"
}

response = requests.post(endpoint, params={'abc':123}, json=data)

print(response.elapsed)
print(response.json())