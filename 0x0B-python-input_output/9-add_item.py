#!/usr/bin/python3
import json
import sys
import os
loadmedaddy = __import__('8-load_from_json_file').load_from_json_file
savemedaddy = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    object = loadmedaddy(filename)
except:
    savemedaddy([], filename)
list = []
for i in range(len(os.sys.argv)):
    if i == 0:
        continue
    list.append(os.sys.argv[i])
savemedaddy(list, filename)
