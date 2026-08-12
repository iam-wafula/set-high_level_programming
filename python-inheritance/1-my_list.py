#!/usr/bin/python3
class MyList(list):
    """A list with a method to print its elements sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
