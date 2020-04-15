#!/usr/bin/python3
import requests
import sys
""" Requests """


r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))
