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
    with open(filename, mode='w', encoding='UTF8') as pr:
        string = json.dumps(my_obj)
        f.write(string)
