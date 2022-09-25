#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    i = 0
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for item in my_list:
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(item)
        i += 1
    return new_list
