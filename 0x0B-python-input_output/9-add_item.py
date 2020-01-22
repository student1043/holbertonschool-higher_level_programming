#!/usr/bin/python3
"""
Adding all arguments to JSON File
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    thisobject = load_from_json_file("add_item.json")
except:
    save_to_json_file([], "add_item.json")
thisobject = load_from_json_file("add_item.json")
my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
thisobject = thisobject + my_list
save_to_json_file(thisobject, "add_item.json")
