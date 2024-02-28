import requests

base_url = 'http://localhost:8000/'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NTIwOTQzLCJpYXQiOjE3MDg1MTczNDMsImp0aSI6ImQwZDY1NzYzNGQ1ZDQwMTJhNzE5NDYyNDhmMzc5MjdhIiwidXNlcl9pZCI6MX0.sJC1oJoV2Df0rqsqPGNDIQoJF_tmnVVISRVNA4RSPjk'
    
    }
result = requests.get(base_url + 'auth/users/me/', headers=headers)

print(result.content)