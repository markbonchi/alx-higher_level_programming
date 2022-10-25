#!/usr/bin/python3
"""To json string module"""


def to_json_string(my_obj):
    """
    to_json_string

    args:
        my_obj: (str)
    """
    import json
    return json.dumps(my_obj)
