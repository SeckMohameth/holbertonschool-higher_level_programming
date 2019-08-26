#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
        m = requests.get(sys.argv[1])
        print("{}".format(m.headers.get('X-Request-Id')))
