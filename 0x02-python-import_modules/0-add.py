#!/usr/bin/python3

if __name__ == "__main__":
    """print the result of 1 and 2."""

    from add_0 import add

    a = 1
    b = 2
    total = add(a,b)
    print("{} + {} = {}".format(a, b, total))

