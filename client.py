import requests

#url='http://localhost:8000/test'
url='https://rcw-eghffbfkfag9fadq.canadacentral-01.azurewebsites.net/'

response = requests.get(url)
response = response.json()
print(response['message'])