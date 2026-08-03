#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.

    Args:
        text: The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip(), end="")
