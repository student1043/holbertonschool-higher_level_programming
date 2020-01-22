#!/usr/bin/python3
import json
import os
loadmedaddy = __import__('8-load_from_json_file').load_from_json_file
savemedaddy = __import__('7-save_to_json_file').save_to_json_file

"""
Save the arguments to the JSON file add_item.json
"""


filename = "add_item.json"
try:
    list = loadmedaddy(filename)
except:
    with open(filename, mode= 'w', encoding='UTF8') as pr:
        pr.write('')
        list = []
if len(os.sys.argv) == 1:
    savemedaddy(list, filename)
else:
    for i in range(1, len(os.sys.argv)):
        list.append(os.sys.argv[i])
    savemedaddy(list, filename)
