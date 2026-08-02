#!/usr/bin/python3
"""
AI Refactoring: The Zen of Python
"""

# Function 1: Sum of even numbers (Verbose)
def sum_even_verbose(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total


# Function 1: Pythonic
# Zen principles:
# - Simple is better than complex.
# - Readability counts.
def sum_even_pythonic(numbers):
    return sum(num for num in numbers if num % 2 == 0)


# Function 2: Longest word (Verbose)
def longest_word_verbose(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# Function 2: Pythonic
# Zen principles:
# - There should be one obvious way to do it.
def longest_word_pythonic(words):
    return max(words, key=len, default="")


# Function 3: Filter positive numbers (Verbose)
def filter_positive_verbose(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


# Function 3: Pythonic
# Zen principles:
# - Beautiful is better than ugly.
# - Readability counts.
def filter_positive_pythonic(numbers):
    return [num for num in numbers if num > 0]


def count_characters(code):
    return len(code.replace(" ", "").replace("\n", ""))


def avg_line_length(code):
    lines = [line for line in code.split("\n") if line.strip()]
    if not lines:
        return 0
    return sum(len(line) for line in lines) / len(lines)


def test_equivalence():
    print(sum_even_verbose([1, 2, 3, 4, 5, 6]))
    print(sum_even_pythonic([1, 2, 3, 4, 5, 6]))

    print(longest_word_verbose(["cat", "elephant", "dog", "whale"]))
    print(longest_word_pythonic(["cat", "elephant", "dog", "whale"]))

    print(filter_positive_verbose([-3, -1, 0, 2, 5, -7]))
    print(filter_positive_pythonic([-3, -1, 0, 2, 5, -7]))


if __name__ == "__main__":
    test_equivalence()
