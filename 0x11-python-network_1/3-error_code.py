#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            print(req.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
