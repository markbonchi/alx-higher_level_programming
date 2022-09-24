#!/usr/bin/python3

def remove_char_at(str, n):
    temp = ""
    if n < 0 or n >= len(str):
        return str
    for item in str:
        if item == str[n]:
            continue
        else:
            temp = temp + item
    return temp
