#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    "Class rectangle"
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        "str function"
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.width, self.height, self.size)

    @property
    def size(self):
        "Getter for size"
        return self.__width

    @size.setter
    def size(self, value):
        'Setter for size'
        self.__width = value
        self.__height = value
