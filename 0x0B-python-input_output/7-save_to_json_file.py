#!/usr/bin/python3
import json
"""
    function that writes an Object to a text file,
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file,
        using a JSON representation
    """
    with open(filename, "w") as pr:
        json.dump(my_obj, pr)
