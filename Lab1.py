import requests

url = input("Enter URL\n")

with requests.get(url) as response:
    headers = response.headers
    print(headers)
