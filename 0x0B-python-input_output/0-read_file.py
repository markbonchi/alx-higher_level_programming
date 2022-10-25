#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    read_file

    args:
        filename: (str)
    """
    import os
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
