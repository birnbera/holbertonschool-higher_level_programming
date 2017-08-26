#!/usr/bin/python3
"""Test module for max_integer function

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Subclass of unittest.TestCase to run tests on
    max_integer function.
    """
    def test_for_docstring(self):
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_sorted(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_desorted(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_wrong_type(self):
        self.assertRaises(TypeError, max_integer, 1234)
        self.assertRaises(TypeError, max_integer, None)

    def test_large_inputs(self):
        self.assertEqual(max_integer([1e100, 4e300, 4e100]), 4e300)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 4.5, 500.2, 300.0]), 500.2)
