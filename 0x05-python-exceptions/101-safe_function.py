#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    a function that executes a function safely
    """
    try:
        res = fct(*args)
        return (res)
    except Exception as err:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
