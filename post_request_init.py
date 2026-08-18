import requests

launch = False

json = {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "role": "viewer"
}

if launch == True:
    response = requests.post(
        url = 'http://localhost:8000/api/v1/auth/register',
        json = json
    )

    print(response.json)

json = {
    "username": "john_doe",
    "password": "securepassword123"
}

response = requests.post(
    url='http://localhost:8000/api/v1/auth/login',
    json=json
)

print(response.json)
print(response.cookies)
