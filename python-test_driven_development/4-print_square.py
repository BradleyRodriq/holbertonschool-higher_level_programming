#!/usr/bin/python3
"""square print"""


def print_square(size):
    """square

    Args:
        size: size of the square
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#", end="")
        for j in range(size):
            print("")
