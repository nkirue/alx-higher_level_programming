#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listord = list(a_dictionary.keys())
    listord.sort()
    for x in listord:
        print("{}: {}".format(x, a_dictionary.get(x)))
