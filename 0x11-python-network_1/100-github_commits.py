#!/usr/bin/python3
import requests
import sys
""" Requests """


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            owner, repo)
    r = requests.get(url)

