#!/usr/bin/python3
""" Print names
This function will print
names that are past to it
and give errors if not strings
"""


def say_my_name(first_name, last_name=""):
    """function that prints a name

    Args:
        first_name: first name string
        last_name: last name string

    Returns:
        nothing

    Raises:
        TypeError: first_name and last_name must be strings

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
