#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tuple_dict = a_dictionary.items()
    garbage = []

    for trash in tuple_dict:
        if trash[1] is value:
            garbage.append(trash[0])

    for key in garbage:
        del a_dictionary[key]
    return a_dictionary
