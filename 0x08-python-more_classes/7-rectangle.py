#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        width = self.__width * 2
        height = self.__height * 2
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return width + height

    def __str__(self):
        new_string = []
        if self.__width is 0 or self.__height is 0:
            return ''
        for x in range(self.__height):
            new_string.append(str(self.print_symbol) * self.width)
        return '\n'.join(new_string)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
