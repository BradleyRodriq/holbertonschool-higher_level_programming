#!/usr/bin/python3
"""Test Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square"""

    def test_square_creation(self):
        sq = Square(5, 2, 3, 1)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 1)

    def test_square_size_property(self):
        sq = Square(5)
        sq.size = 10
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)

    def test_square_update_args(self):
        sq = Square(5, 2, 3, 1)
        sq.update(10, 20, 30, 40)
        self.assertEqual(sq.id, 10)
        self.assertEqual(sq.size, 20)
        self.assertEqual(sq.x, 30)
        self.assertEqual(sq.y, 40)

    def test_square_update_kwargs(self):
        sq = Square(5, 2, 3, 1)
        sq.update(id=10, size=20, x=30, y=40)
        self.assertEqual(sq.id, 10)
        self.assertEqual(sq.size, 20)
        self.assertEqual(sq.x, 30)
        self.assertEqual(sq.y, 40)

    def test_square_to_dictionary(self):
        sq = Square(5, 2, 3, 1)
        sq_dict = sq.to_dictionary()
        self.assertEqual(sq_dict, {"id": 1, "size": 5, "x": 2, "y": 3})

    def test_square_string_representation(self):
        sq = Square(5, 2, 3, 1)
        self.assertEqual(str(sq), "[Square] (1) 2/3 - 5")

if __name__ == '__main__':
    unittest.main()
