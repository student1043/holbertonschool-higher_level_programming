#!/usr/bin/python3
import requests
import sys
""" Requests """


r = requests.post(sys.argv[1], data = {'email':sys.argv[2]})
print(r.text)

