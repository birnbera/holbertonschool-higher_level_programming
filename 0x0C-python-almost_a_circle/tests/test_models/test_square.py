#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
import sys
from io import StringIO
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """Subclass of unittest.TestCase to test Square class functionality"""
    def setUp(self):
        """Redirect stdout to readable buffer to check output of
        methods relying on print function."""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file stream to
        sys.stdout so printing goes to the screen as before."""
        sys.stdout = sys.__stdout__

    def test_str(self):
        """Test that __str__ magic method produces correct output."""
        Base._Base__nb_object = 0
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s2.__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(s3.__str__(), "[Square] (3) 1/3 - 3")

    def test_area(self):
        """Test that area method returns correct values"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)

    def test_display_offset(self):
        """Test that the `display()` method prints correct output and
        uses offset values when specified. Relies on redirecting stdout
        to StringIO instance for comparing with expected output.
        Wraps calls to display and comparison with stdout in try/finally
        in order to reset stdout to beginning of stream even if the test
        fails.
        """
        Base._Base__nb_object = 0
        s1 = Square(5)
        s1_out = "#####\n" \
                 "#####\n" \
                 "#####\n" \
                 "#####\n" \
                 "#####\n"

        s2 = Square(2, 2)
        s2_out = "  ##\n" \
                 "  ##\n"

        s3 = Square(3, 1, 3)
        s3_out = "\n\n\n" \
                 " ###\n" \
                 " ###\n" \
                 " ###\n"

        try:
            s1.display()
            self.assertEqual(sys.stdout.getvalue(), s1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            s2.display()
            self.assertEqual(sys.stdout.getvalue(), s2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            s3.display()
            self.assertEqual(sys.stdout.getvalue(), s3_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_size(self):
        """Test that Square `size` attribute is set correctly"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 10")
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.size = "9"

    def test_update_args_kwargs(self):
        """Test that `update()` method correctly handles *args and **kwargs"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")

    def test_to_dict(self):
        """Test that `to_dictionary()` method produces valid dictionary
        representation of Square instance. Converts to dictionary and
        updates distinct instance to those values and compares the two
        resulting objects to show that they have the same attributes but
        are not identical objects.
        """
        Base._Base__nb_object = 0
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/1 - 10")
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'x': 2,
                                              'size': 10, 'y': 1})
        self.assertIs(type(s1.to_dictionary()), dict)
        s2 = Square(1, 1)
        self.assertEqual(s2.__str__(), "[Square] (2) 1/0 - 1")
        s2.update(**s1.to_dictionary())
        self.assertEqual(s2.__str__(), "[Square] (1) 2/1 - 10")
        self.assertNotEqual(s1, s2)
