#!/usr/bin/python3
"""Model rectangle"""
from models.base import Base

class Rectangle(Base):
    """Rectanle class

    Args:
    width

    Raises:

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method to set attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value




    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value



    @property
    def x(self):
        """ getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x"""
        if value < 0            raise ValueError("x must be >= 0")
        elif type(value) is not int:
            raise TypeError("x must be an integer")
        else:
            self.__x = value



    @property
    def y(self):
        """y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if value < 0:
            raise ValueError("y must be >= 0")
        elif type(value) is not int:
            raise TypeError("y must be an integer")
        else:
            self.__y = value


    def area(self):
        """Return area"""
        return self.width * self.height

    def display(self):
        """Changing the display for #"""
        print('\n' * self.y, end='')
        for n in range(self.height):
            print(' ' * self.x + "#" * self.width)


    def __str__(self):
        """Overriding the __str__ method"""
        return ("[{}] ({}) {}/{} - {}/{}".format\
(Rectangle.__name__, self.id, self.x, self.y, self.width, self.height))



    def update(self, *args, **kwargs):
        """update class and assign arguments"""

        i = 0
        for idx in args:
            i += 1
            if i == 1:
                self.id = idx
            if i == 2:
                self.width = idx
            if i == 3:
                self.height = idx
            if i == 4:
                self.x = idx
            if i == 5:
                self.y = idx
