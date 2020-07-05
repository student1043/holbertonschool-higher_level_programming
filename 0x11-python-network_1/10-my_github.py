#!/usr/bin/python3
import requests
import sys
""" Requests """


if __name__ == "__main__":
    """ Requests """
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    response = r.json()
    print(response.get('id'))
