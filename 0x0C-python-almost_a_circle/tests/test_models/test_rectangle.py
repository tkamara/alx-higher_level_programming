#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
import sys
import io
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    def test_setup(self):
        r = Rectangle(1, 2, 3, 4, 5)

    def test_to_dict(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r1 = r.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r1, exp)

    def test_to_dict_1(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r1 = r.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(type(r1).__name__, type(exp).__name__)

    def test_area(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.area(), 2)

    def test_delete(self):
        r = Rectangle(1, 2, 3, 4, 5)
        del r
        Base._Base__nb_objects = 0
