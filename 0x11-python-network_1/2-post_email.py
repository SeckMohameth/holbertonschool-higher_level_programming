#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    mail = {'email': email}
    data = urllib.parse.urlencode(mail)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode('utf-8'))
