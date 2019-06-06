#!/usr/bin/python3
import 7-base_geometry.py

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    integer_validator(self, height, height)
    integer_validator(self, width, width)
