#!/usr/bin/python3
"""Module that prints a string in uppercase."""


def uppercase(str):
    """Print the given value in uppercase, followed by a new line."""
    str = "{}".format(str)
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:c}".format(ord(c)), end="")
    print()
