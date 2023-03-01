import requests

url = input("Enter URL\n")

with requests.get(url) as response:
    headers = dict(response.headers)
    cookies = response.cookies
    for i in headers.keys():
        print("{}: {}".format(i,headers[i]))
    print("\nWeb server software: {}".format(headers['Server']))
    if "Set-Cookie" in headers.keys():
        print("\nThe site uses cookies.\n")
        for cookie in response.cookies:
            print("Cookie name: {}  Expiry: {}".format(cookie.name, cookie.expires))
    else:
        print("\nThe site doesn't use cookies.")
