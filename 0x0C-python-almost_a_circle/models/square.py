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
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        "Getter for size"
        return self.width

    @size.setter
    def size(self, value):
        'Setter for size'
        self.width = value
        self.height = value
