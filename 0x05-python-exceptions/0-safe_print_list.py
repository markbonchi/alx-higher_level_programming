#!/ussr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end='')
    except:
        return i
    else:
        return i + 1
    finally:
        print()
