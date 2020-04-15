#!/usr/bin/python3
import urllib.request
"""URL Fetch"""


if __name__ == "__main__":
    """Fetch URL"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    orint("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf8')))

