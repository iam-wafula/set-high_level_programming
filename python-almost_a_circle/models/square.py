#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update attributes."""
        attrs = ["id", "size", "x", "y"]

        if args:
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
