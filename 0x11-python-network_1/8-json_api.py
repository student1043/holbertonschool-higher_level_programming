#!/usr/bin/python3
import requests
import sys
""" Requests """


if __name__ = "__main__":
    """ Requests """
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        mydata = sys.argv[1]
    else:
        mydata = ""
    q = {'q': mydata}
    r = requests.post(url, data=q)
    try:
        json_response = r.json()
        if json_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_response['id'], json_response['name']))
    except ValueError:
        print("Not a valid JSON")
