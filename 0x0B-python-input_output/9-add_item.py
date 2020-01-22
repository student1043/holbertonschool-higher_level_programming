#!/usr/bin/python3
import json
import os
l = __import__('8-load_from_json_file').load_from_json_file
s = __import__('7-save_to_json_file').save_to_json_file

"""
Adding arguments to a JSON file add_item.json
"""

filename = "add_item.json"
try:
    object = l(filename)
except:
    with open(filename, mode='w', encoding='UTF8') as pr:
        pr.write('')
        object = []
if len(os.sys.argv) == 1:
    s(object, filename)
else:
    for i in range(1, len(os.sys.argv)):
        object.append(os.sys.argv[i])
    s(object, filename)
