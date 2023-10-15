#!/usr/bin/python3
'''task 7 module'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1;])

try:
        old_date = load_from_json_file('add_item.json')
except Exception:
        old_date = []

old_date.extend(arglist)
save_to_json_file(old_date, 'add_item.json')
