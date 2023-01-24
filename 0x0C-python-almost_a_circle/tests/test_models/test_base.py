#!/usr/bin/python3
"""
Unit testing for base.py
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    testing the Base class instantiation
    """
    def test_arg_num(self):
        a1 = Base()
        a2 = Base()
        self.assertEqual(a1.id, a2.id - 1)

    def test_none_id(self):
        a1 = Base(None)
        a2 = Base(None)
        self.assertEqual(a1.id, a2.id - 1)

    def test_three_bases(self):
        a1 = Base()
        a2 = Base()
        a3 = Base()
        self.assertEqual(a1.id, a3.id - 2)

    def test_unique_id(self):
        self.assertEqual(5, Base(5).id)

    def test_id_public(self):
        a1 = Base(2)
        a1.id = 23
        self.assertEqual(23, a1.id)
