#!/usr/bin/python3
import requests
import sys
""" Requests """

if __name__ == "__main__":
    """ Request """
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
