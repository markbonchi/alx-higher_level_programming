#!/usr/bin/python3
"""Save to json file module"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file

    args:
        my_obj: (obj)
        filename: (str)
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
