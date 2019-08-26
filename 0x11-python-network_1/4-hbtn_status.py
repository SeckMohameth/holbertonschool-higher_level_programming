#!/usr/bin/python3
import requests
if __name__ == "__main__":
        html = requests.get('https://intranet.hbtn.io/status').text
        print("Body repsonse:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
