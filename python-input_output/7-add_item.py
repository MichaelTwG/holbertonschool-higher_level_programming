#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

""" CREATE A LIST TO CONVERT """
len_arg = len(sys.argv)
JSON_list = []

for arg in range(1, len_arg):
   JSON_list.append(sys.argv[arg])
   
save_to_json_file(JSON_list, "add_item.json")