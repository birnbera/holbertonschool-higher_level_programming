#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from models.base import Base
try:  # Uses Rectangle instance for `test_to_json_string`
    from models.rectangle import Rectangle
except ImportError:  # Skip test if Rectangle unavailable or not implemented
    DONT_RUN = True
else:
    DONT_RUN = False
import json
"""Unit tests for Base class"""


class TestBase(unittest.TestCase):
    """Subclass of unittest.TestCase to test Base class functionality"""
    def setUp(self):
        """Redirect stdout to readable buffer to check output of
        methods relying on print function."""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file stream to
        sys.stdout so printing goes to the screen as before."""
        sys.stdout = sys.__stdout__

    def test_id(self):
        """Test for id property"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

    @unittest.skipIf(DONT_RUN is True, "Rectangle class not yet implemented")
    def test_to_json_string(self):
        """Test for conversion of Base subclasses to json representation.
        Assumes that subclasses have implemented `to_dictionary()` method.
        If Rectangle class is not available do not run this test.
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {'x': 2, 'width': 10,
                                       'id': 1, 'height': 7,
                                       'y': 8})
            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 10, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                               '"y": 8}]'))
