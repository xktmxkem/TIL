import requests
from requests.api import request

url = 'https://api.agify.io?name=taehun'

response = requests.get(url).json()

print(response['name'])