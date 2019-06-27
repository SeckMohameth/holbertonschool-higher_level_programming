#!/usr/bin/python3

import unittest
from models.rectangle import Ractangle

"""Unit Test for rectangle"""

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(2,2)
        self.assertEqual(r.area, 4)
        r2 = Rectangle(2,4)
        self.assertEqual(r.area, 8)

    def test_for_str(self):
        new_rect = Retangle(2, "3")
        self.assertRaises(ValueError)
