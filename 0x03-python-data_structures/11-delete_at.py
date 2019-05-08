#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    new_list = my_list
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list.remove(idx)
    return new_list
