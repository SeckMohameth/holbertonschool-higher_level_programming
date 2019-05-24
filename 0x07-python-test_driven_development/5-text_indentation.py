#!/usr/bin/python3
"""a function that prints
a text with 2 new lines after each
 of these characters: ., ? and :
"""

def text_indentation(text):


    suffix = ['.', '?', ':']

    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i in suffix:
            print('\n')
            print("{}".format(i))
