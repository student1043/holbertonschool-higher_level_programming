#!/usr/bin/python3
import json
"""
    function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”
    """
    with open(filename, "r") as pr:
        data = pr.read()
        return json.loads(data)
