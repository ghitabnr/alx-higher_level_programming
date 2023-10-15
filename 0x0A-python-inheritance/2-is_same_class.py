#!/usr/bin/python3
"""Defines a function that returns True if the object is exactly an instance
   of the specified class; otherwise False."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class; otherwise False.

    Args:
            obj (any): object to check
            a_class (type): class to match the type of obj to

    Returns:
            If obj is exactly an instance of a_class - True.
            Otherwise - False.
    """
    return type(obj) is a_class
