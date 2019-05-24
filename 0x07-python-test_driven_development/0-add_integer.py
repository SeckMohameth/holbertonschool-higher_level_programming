#!/usr/bin/python3
"""Program to add two numbers.
Checking if both are int and floats
and then casting them to ints
"""


def add_integer(a, b=98):
    """ function to add integers


    Args:
        a (int): The first number/parameter
        b (int): Second number/parameter

    Returns:
        a + b

    Raises:
        TypeError: Wrong type if not int or
        float
    """

    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
