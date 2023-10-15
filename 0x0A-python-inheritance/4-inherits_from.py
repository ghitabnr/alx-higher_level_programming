#!/usr/bin/python3
"""Defines a function that returns True
   if the object is an instance of,
   or if the object is an instance of
   a class that inherited from,
   the specified class; otherwise False."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of, or if obj is an
      instance of a class that inherited from,
      a_class. Otherwise, return False.

    Args:
         obj (any): object to check
         a_class (type): class to match the type of obj to

    Returns:
            If obj is an instance of, or if obj is an
            instance of a class that
            inherited from, a_class - True.
            Otherwise - False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
