#!/usr/bin/python3

def no_c(my_string):
    temp = ""
    for item in my_string:
        if item in ('c', 'C'):
            continue
        temp = temp + item
    return temp
