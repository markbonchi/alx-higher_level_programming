#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    this_list = dir(hidden_4)
    for item in this_list.sort():
        if item[0] != "_" and item[1] != "_":
            print(item)
