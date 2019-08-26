#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email_address = sys.argv[2]
    mail = {'email': email_address}
    mine = requests.post(url, data=email_address)
    print("{}".format(mine.text))
