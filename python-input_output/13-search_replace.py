#!/usr/bin/python3
"""Module that inserts a line of text after a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string."""
    new_text = ""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_text)
