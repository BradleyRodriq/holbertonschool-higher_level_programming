#!/usr/bin/python3
"""unittests for rectangle.py"""
import sys
import io
from typing import Type
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_rectangle(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_rect_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_rect_two_args(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_three_args(self):
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(3, 2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_four_args(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_five_args(self):
        self.assertEqual(5, Rectangle(1, 2, 3, 4, 5).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangle_sizes(unittest.TestCase):
    """Test Rectangle"""

    def test_no_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_no_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)


class TestRectangle_xy(unittest.TestCase):
    """Test Rectangle"""

    def test_no_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 4)

    def test_no_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 3, -2, 1)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 3, 2, -1)


class TestRectangle_area(unittest.TestCase):
    """Test Rectangle"""

    def test_area(self):
        rect = Rectangle(10, 2)
        self.assertEqual(20, rect.area())

class TestRectangle_str(unittest.TestCase):
    """Test Rectangle"""

    def test_str_method_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.__str__(1)

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        rect = Rectangle(1, 2)
        capture = TestRectangle_str.capture_stdout(rect, "print")
        correct = "[Rectangle] ({}) 0/0 - 1/2\n".format(rect.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        rect = Rectangle(1, 2, 3)
        correct = "[Rectangle] ({}) 3/0 - 1/2".format(rect.id)
        self.assertEqual(correct, rect.__str__())

    def test_str_method_width_height_x_y(self):
        rect = Rectangle(1, 2, 3, 4)
        correct = "[Rectangle] ({}) 3/4 - 1/2".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_str_method_width_height_x_y_id(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rect))


class TestRectangle_update(unittest.TestCase):

    def test_update_args_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect))

    def test_update_args_one(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rect))

    def test_update_args_two(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(1, 2)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rect))

    def test_update_args_three(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(1, 2, 3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/3", str(rect))

    def test_update_args_four(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(1, 2, 3, 4)
        self.assertEqual("[Rectangle] (1) 4/10 - 2/3", str(rect))

    def test_update_args_five(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(rect))

    def test_update_args_more_than_five(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(1, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(rect))

    def test_update_kwargs_one(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rect))

    def test_update_kwargs_two(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rect))

    def test_update_kwargs_three(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=3, width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/3", str(rect))

    def test_update_kwargs_four(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=3, width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/3", str(rect))

    def test_update_kwargs_five(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rect))
