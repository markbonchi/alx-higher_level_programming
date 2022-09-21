#!/usr/bin/python3

for i in range(100):
    if i < 10:
        print("0{0}".format(i), end= ', ')
    elif i != 99:
        print("{0}".format(i), end= ', ')
    else:
        print(i)
