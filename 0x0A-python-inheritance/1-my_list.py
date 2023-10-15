#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Represent a list."""

    def print_sorted(self):
        """Print a sorted list."""
        print(sorted(self))
