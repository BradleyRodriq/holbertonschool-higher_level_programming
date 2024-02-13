#!/usr/bin/python3
"""base"""


import json

class Base:
    """
    Base class for all other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The ID of the instance. If not provided,
                a unique ID will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
