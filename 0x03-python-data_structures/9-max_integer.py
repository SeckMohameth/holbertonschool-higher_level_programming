#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    myMax = my_list[0]
    for x in my_list:
        if myMax <= x:
            myMax = x
    return myMax
