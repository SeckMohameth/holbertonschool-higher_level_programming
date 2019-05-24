#!/usr/bin/python3

import unittest


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(list=[1, 3, 32, 45]):
        list.assertEqual(45)
