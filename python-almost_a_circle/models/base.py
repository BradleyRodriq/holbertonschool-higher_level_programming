#!/usr/bin/python3
"""base"""


class Base:
    """base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init

        Args:
            self: instance
            id: instance id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
