#!/usr/bin/python3
"""append write file module"""


def append_write(filename="", text=""):
    """
    append_write

    args:
        filrname: (str)
        text: (str)
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
