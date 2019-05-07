#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for x in new_string:
        if x is 'c' or x is 'C':
            new_string.remove(x)
    s = ""
    new_string = s.join(new_string)
    return(new_string)
