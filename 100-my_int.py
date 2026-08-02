#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """A rebel integer class that inverts == and != operators."""

    def __eq__(self, other):
        """Return the inverse of the equality comparison."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return the inverse of the inequality comparison."""
        return super().__eq__(other)
