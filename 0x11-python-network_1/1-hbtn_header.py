#!/usr/bin/python3
import urllib.request
import sys
"""URL header"""


if __name__ == "__main__":
        """Fetch Header"""
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.getheader('X-Request-Id'))
