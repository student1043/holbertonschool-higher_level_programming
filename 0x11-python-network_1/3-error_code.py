#!/usr/bin/python3
import urllib.request
import sys
"""URL header"""


if __name__ == "__main__":
    """Fetch Header"""
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
