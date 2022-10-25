#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """
    write_file

    args:
        filrname: (str)
        text: (str)
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
