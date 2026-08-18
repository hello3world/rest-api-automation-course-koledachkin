import requests
from pprint import pprint

response = requests.get("http://localhost:8000/api/v1/health")

response_json = response.json()
response_text = response.text
response_code = response.status_code
response_headers = response.headers
response_cookies = response.cookies

pprint(response_json)
pprint(response_text)
pprint(response_code)
pprint(response_headers)
pprint(response_cookies)

assert response_code == 200
assert response_json["status"] == 'healthy'
