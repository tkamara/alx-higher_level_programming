#!/usr/bin/python3
"""Unittest for max integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    The different test cases
    """

    def test_max_first(self):
        """
        testing max int at the beginning
        """
        num = [5, 4, 3, 2]
        self.assertEqual(max_integer(num), 5)

    def test_max_last(self):
        """
        testing max int at the end
        """
        num = [2, 3, 4, 5]
        self.assertEqual(max_integer(num), 5)

    def test_max_middle(self):
        """
        testing max int at the middle
        """
        num = [3, 4, 5, 2]
        self.assertEqual(max_integer(num), 5)

    def test_max_string(self):
        """
        testing with a string in the list
        """
        num = ["3", 4, 5, 2]
        with self.assertRaises(TypeError):
            max_integer(num)

    def test_empty_list(self):
        """
        testing an empty list
        """
        num = []
        self.assertEqual(max_integer(num), None)


