#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret_list = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            ret_list.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            ret_list.append(0)
            continue
        except IndexError:
            print("out of range")
            break
        except Exception as e:
            print(e)
            ret_list.append(0)
            continue
        else:
            ret_list.append(value)
    return ret_list
