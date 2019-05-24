#!/usr/bin/python3
"""a function that prints
a text with 2 new lines after each
 of these characters: ., ? and :
"""

def text_indentation(text):

    last = 0

    suffix = ['.', '?', ':']

    if type(text) is not str:
        raise TypeError("text must be a string")
    for idx, l in enumerate(text):
        if l in suffix:
            print(text[last:idx + 1].strip() + '\n')
            last = idx + 1
    print(text[last:].strip(), end="")
