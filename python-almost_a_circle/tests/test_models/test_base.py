#!/usr/bin/python3
"""unittests for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """TestBase"""

    def test_zero_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_no_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Test Base"""

    def test_to_json_string_rectrangle_type(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(str, type(
                                Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_square_type(self):
        sq = Square(5, 4, 3, 2)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))


class TestBase_save_to_file(unittest.TestCase):
    """Test Base"""

    def test_save_to_file_rectangle(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read())) == 53

    def test_save_to_file_square(self):
        sq = Square(5, 4, 3, 2)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read())) == 39

    def save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Test Base"""

    def test_from_json_string_rectangle(self):
        list = [{"id": 5, "width": 4, "height": 3, "x": 2, "y": 1}]
        input = Rectangle.to_json_string(list)
        output = Rectangle.from_json_string(input)
        self.assertEqual(list, output)

    def test_from_json_string_square(self):
        list = [{"id": 5, "size": 4, "x": 2, "y": 1}]
        input = Square.to_json_string(list)
        output = Square.from_json_string(input)
        self.assertEqual(list, output)

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))


class TestBase_create(unittest.TestCase):
    """Test Base"""

    def test_create_rectangle(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect_dict = rect.to_dictionary()
        created_rect = Rectangle.create(**rect_dict)
        self.assertEqual("[Rectangle] (1) 3/2 - 5/4", str(rect))

    def test_create_square(self):
        sq = Square(5, 4, 3, 2)
        sq_dict = sq.to_dictionary()
        created_sq = Square.create(**sq_dict)
        self.assertEqual("[Square] (2) 4/3 - 5", str(sq))


class TestBase_load_from_file(unittest.TestCase):
    """Test Base"""

    def test_load_from_file_rectangle(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect2 = Rectangle(6, 7, 8, 9, 0)
        Rectangle.save_to_file([rect, rect2])
        rect_list = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(rect_list[1]))

    def test_load_from_file_square(self):
        sq = Square(5, 4, 3, 2)
        sq2 = Square(6, 7, 8, 9)
        Square.save_to_file([sq, sq2])
        sq_list = Square.load_from_file()
        self.assertEqual(str(sq2), str(sq_list[1]))

if __name__ == '__main__':
    unittest.main()
