#!/usr/bin/python3

key = 0
while key < 26:
    match = 0
    if key % 2 != 0:
        match = ord('a') - ord('A')
    print("{}".format(chr(ord('z') - match - key)), end='')
    key += 1
