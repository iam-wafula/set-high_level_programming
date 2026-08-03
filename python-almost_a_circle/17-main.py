#!/usr/bin/python3
"""17-main"""

from models.rectangle import Rectangle

if __name__ == "__main__":
    list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
    ]

    for dictionary in list_input:
        obj = Rectangle.create(**dictionary)
        print("[{}] {}".format(type(obj), obj))
        print(obj.to_dictionary())
