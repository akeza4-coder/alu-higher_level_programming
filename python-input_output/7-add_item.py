#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then saves them to a file.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Extend the list with all arguments except the script name (sys.argv[0])
items.extend(sys.argv[1:])

save_to_json_file(items, filename)
