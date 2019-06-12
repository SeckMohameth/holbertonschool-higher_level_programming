#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        #Checking input for id
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.asserEqual(b2.id, 2)

    def test_more_args(self):
        with self.assertRaises(TypeError, msg ='...'):
            Base(1,2)

    def setUp(self):
        Base.__Base.nb_objects = 0
