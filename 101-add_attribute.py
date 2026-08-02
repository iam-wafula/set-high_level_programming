#!/usr/bin/python3
"""Module that defines the add_attribute function."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object.

    Args:
        obj: The object to modify.
        name (str): The attribute name.
        value: The value to assign.

    Raises:
        TypeError: If the object does not allow new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
