#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
import sys
import os
import json
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Subclass of unittest.TestCase to test Rectangle class functionality"""
    def setUp(self):
        """Redirect stdout to readable buffer to check output of
        methods relying on print function."""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file stream to
        sys.stdout so printing goes to the screen as before."""
        sys.stdout = sys.__stdout__

    def test_id(self):
        """Test for id property. Set class variable __nb_object to 0 so id
        values are as expected"""
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_raise(self):
        """Test that instances raise correct errors and messages for incorrect
        input values."""
        Rectangle._Base__nb_object = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(10, 2, {})
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test that area method returns correct values"""
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test that display method prints correct output. Relies on
        redirecting stdout to StringIO instance for comparing with
        expected output. Wraps calls to display and comparison with
        stdout in try/finally in order to reset stdout to beginning of
        stream even if the test fails.
        """
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(4, 6)
        r1_out = "####\n" \
                 "####\n" \
                 "####\n" \
                 "####\n" \
                 "####\n" \
                 "####\n"
        r2 = Rectangle(2, 2)
        r2_out = "##\n" \
                 "##\n"
        try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), r1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r2.display()
            self.assertEqual(sys.stdout.getvalue(), r2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_str(self):
        """Test that __str__ magic method produces correct output."""
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_offset(self):
        """Test that `display()` method correctly works with offset values.
        As with `test_display`, `test_display_offset` relies on stdout being
        redirected to a StringIO instance. See `test_display` for details.
        """
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(2, 3, 2, 2)
        r1_out = "\n" \
                 "\n" \
                 "  ##\n" \
                 "  ##\n" \
                 "  ##\n"
        r2 = Rectangle(3, 2, 1, 0)
        r2_out = " ###\n" \
                 " ###\n"
        try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), r1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r2.display()
            self.assertEqual(sys.stdout.getvalue(), r2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_update1(self):
        """Test that `update()` method works with *args unpacking"""
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update2(self):
        """Test that `update()` method works with **kwargs unpacking."""
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dict(self):
        """Test that `to_dictionary()` method produces valid dictionary
        representation of Rectangle instance. Converts to dictionary and
        updates distinct instance to those values and compares the two
        resulting objects to show that they have the same attributes but
        are not identical objects.
        """
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9,
                                              'id': 1, 'height': 2,
                                              'width': 10})
        self.assertIs(type(r1.to_dictionary()), dict)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1.to_dictionary())
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)

    def test_save_to_file(self):
        """Test that `save_to_file()` method of Rectangle instance
        can be used to directly serialize and write to a file. Removes
        file after test if test was able to write to disk.
        """
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertIs(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[{"y": 8, '
                                        '"x": 2, '
                                        '"id": 1, '
                                        '"width": 10, '
                                        '"height": 7}, '
                                        '{"y": 0, '
                                        '"x": 0, '
                                        '"id": 2, '
                                        '"width": 2, '
                                        '"height": 4}]'))
        os.remove("Rectangle.json")
