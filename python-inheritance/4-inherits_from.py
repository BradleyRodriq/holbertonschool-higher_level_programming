#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from

    Args:
        obj: object to check
        a_class: class to check against
    """
    """if isinstance(type(obj), a_class)"""
    if type(obj) != a_class:
        return True
    return False
