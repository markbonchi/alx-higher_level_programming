#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    i = 0
    while i < len(my_list):
        if i > 0:
            if my_list[i] > max_num:
                max_num = my_list[i]
        else:
            max_num = my_list[i]
        i += 1
    return max_num
