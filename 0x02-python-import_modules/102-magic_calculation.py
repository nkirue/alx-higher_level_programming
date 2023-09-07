#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        ci = add(a, b)
        for x in range(4, 6):
            ci = add(ci, x)
        return (ci)
    else:
        return sub(a, b)
