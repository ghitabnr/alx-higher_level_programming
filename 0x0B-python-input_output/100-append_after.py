#!usr/bin/python3
"""appden after a string"""


def append_after(filename="", search_string="", new_string=""):
    """appden after a string"""
    new_str = ""
    with open(filename, "r") as f:
        for line in f:
            new_str += line
            if search_string in line:
                new_str += new_string
    with open(filename, "w") as f:
        f.write(new_str)
