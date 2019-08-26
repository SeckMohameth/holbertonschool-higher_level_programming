#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body repsonse:")
        print("\t- type: {}".format(type(html)))
        print("\t- tcontent: {}".format(html))
