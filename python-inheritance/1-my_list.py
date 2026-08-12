#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """A list subclass with a sorted-print method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
