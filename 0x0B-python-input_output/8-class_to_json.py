#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """
    class_to_json

    args:
        obj: (object)
    """
    return obj.__dict__
