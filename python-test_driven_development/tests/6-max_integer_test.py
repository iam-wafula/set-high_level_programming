#!/usr/bin/python3
"""Unittests for max_integer."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 10, 3]), 10)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([3, 5, 5, 2]), 5)


if __name__ == "__main__":
    unittest.main()
