#!/usr/bin/python3
import requests
import sys
""" Requests """


if __name__ = "__main__":
    """ Requests """
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1]
    if json.loads(q):
        print("[{}] {}".format(q.id, q.user))
