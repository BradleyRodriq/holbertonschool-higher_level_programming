#!/usr/bin/python3
"""Test Square"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square"""
    def test_is_square(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_square2(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        sq1 = Square(10)
        sq2 = Square(11)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_two_args(self):
        sq1 = Square(10, 2)
        sq2 = Square(2, 10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_three_args(self):
        sq1 = Square(10, 2, 2)
        sq2 = Square(2, 2, 10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquare_size(unittest.TestCase):
    """Test Square"""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_xy(unittest.TestProgram):
    """Test Square"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquare_area(unittest.TestCase):
    """Test Square"""
    def test_area(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())


class TestSquare_stdout(unittest.TestCase):
    """Test Square"""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        sq = Square(4)
        capture = TestSquare_stdout.capture_stdout(sq, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(sq.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        sq = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(sq.id)
        self.assertEqual(correct, sq.__str__())

    def test_str_method_size_x_y(self):
        sq = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_str_method_size_x_y_id(self):
        sq = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sq))

    def test_str_method_changed_attributes(self):
        sq = Square(7, 0, 0, [4])
        sq.size = 15
        sq.x = 8
        sq.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(sq))

    def test_str_method_one_arg(self):
        sq = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            sq.__str__(1)

    def test_display_one_arg(self):
        sq = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sq.display(1)


class TestSquare_update_args_kwargs(unittest.TestCase):
    """Test Square"""

    def test_update_args_zero(self):
        sq = Square(10, 10, 10, 10)
        sq.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq))

    def test_update_args_one(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(sq))

    def test_update_args_two(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sq))

    def test_update_args_three(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(sq))

    def test_update_args_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def test_update_args_more_than_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def test_update_kwargs_one(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(sq))

    def test_update_kwargs_two(self):
        sq = Square(10, 10, 10, 10)
        sq.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(sq))

    def test_update_kwargs_three(self):
        sq = Square(10, 10, 10, 10)
        sq.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(sq))

    def test_update_kwargs_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(sq))


class TestSquare_to_dictionary(unittest.TestCase):
    """Test Square"""

    def test_to_dictionary_output(self):
        sq = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, sq.to_dictionary())


if __name__ == '__main__':
    unittest.main()
