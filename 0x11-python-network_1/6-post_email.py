#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    mail = {'email': sys.argv[2]}
    mine = requests.post(sys.argv[1], data=mail)
    print("{}".format(mine.text))
