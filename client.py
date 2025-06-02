import requests

url='http://localhost:8000'

response = requests.get(url)
response = response.json()
print(response['message'])