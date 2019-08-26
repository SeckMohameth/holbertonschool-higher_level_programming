#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    url = request.get(sys.argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(url.text)
