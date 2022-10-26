#!/usr/bin/python3
"""add item module"""


import json
from sys import argv
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    with open(filename, "w", encoding="utf-8") as f:
        try:
            my_list = load_json(filename)
        except Exception as err:
            f.write(json.dumps(argv[1:]))
        else:
            new_list = my_list + argv[1:]
            save_json(new_list, filename)
