#!/usr/bin/python3
import requests
import sys
""" Requests """


if __name__ == "__main__":
    """ Requests """
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))

