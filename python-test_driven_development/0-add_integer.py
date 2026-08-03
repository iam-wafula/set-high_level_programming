#!/usr/bin/python3
"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    """Return the sum of two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
