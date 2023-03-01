import requests

url = 'http://python.org/'

with requests.get(url) as response:
    headers = response.headers
    print(headers)
