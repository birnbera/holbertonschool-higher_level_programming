#!/usr/bin/python3
import unittest
import sys
import os
import json
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_id(self):
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_raise(self):
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
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
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
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_offset(self):
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
