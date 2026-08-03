#!/usr/bin/python3
"""18-main"""

from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)

    Rectangle.save_to_file([r1, r2])

    rectangles = Rectangle.load_from_file()

    for rectangle in rectangles:
        print(rectangle)
