#!/usr/bin/python3
'''Module 7-add_item'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


JSON_list = []

for arg in range(1, len(sys.argv)):
    JSON_list.append(sys.argv[arg])
try:
    JSON_list2 = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file([], "add_item.json")
JSON_list2 += JSON_list
save_to_json_file(JSON_list2, "add_item.json")
