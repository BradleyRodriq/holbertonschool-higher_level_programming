#!/usr/bin/python3
"""addition"""


def add_integer(a, b=98):
    """addition of a and b

    Args:
        a: first number
        b: second number
    """
    if not isinstance(a, int, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
