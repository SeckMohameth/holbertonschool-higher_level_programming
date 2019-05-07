#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    myMax = 0
    for x in my_list:
        if myMax < x:
            myMax = x
    return myMax
