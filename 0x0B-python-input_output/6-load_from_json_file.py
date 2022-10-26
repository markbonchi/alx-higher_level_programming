#!/usr/bin/python3
"""Load from json file module"""


def load_from_json_file(filename):
    """
    load_from_json_file

    args:
        filename: (str)
    """
    import json

    with open(filename, "r", encoding="utf-8") as f:
        my_file = f.read()
        return json.loads(my_file)
