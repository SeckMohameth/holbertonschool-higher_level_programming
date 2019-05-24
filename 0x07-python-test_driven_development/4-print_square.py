#!/usr/bin/python3
"""a function that prints a square with the character #
"""


def print_square(size):
    """a function that prints a square with #
    character.

    Args:
        size: is the size length of the square

    Returns:
        nothing

    Raises:
        TypeError: size must be an integer
        size must be an integer

        ValueError: size must be >= 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for x in range(size):
            print("#" * size)
