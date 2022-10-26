#!/usr/bin/python3
"""From json string module"""


def from_json_string(my_str):
    """
    from_json_string

    args:
        my_str: (str)
    """
    import json
    return json.loads(my_str)
