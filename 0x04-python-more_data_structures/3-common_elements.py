#!/usr/bin/python3
def common_elements(set_1, set_2):
    myset = set()
    for element in set_1:
        for element2 in set_2:
            if element is element2:
                myset.add(element)
                return myset
