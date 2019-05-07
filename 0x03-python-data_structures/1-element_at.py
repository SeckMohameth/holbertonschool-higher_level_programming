#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list == None and idx == None:
        return None

    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    for x in my_list:
        return my_list[idx]
