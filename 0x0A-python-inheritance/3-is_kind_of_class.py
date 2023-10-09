#!/usr/bin/python3
"""This defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """This check if an object is an instance or inherited """
    if isinstance(obj, a_class):
        return True
    return False
