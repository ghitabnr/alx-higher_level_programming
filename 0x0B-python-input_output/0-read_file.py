#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """read_file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
