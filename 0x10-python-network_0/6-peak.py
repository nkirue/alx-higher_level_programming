#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
   lo_ = 0
    hi = len(list_of_integers)
    cen = ((hi -lo_) // 2) +lo_
    cen = int(cen)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[cen] >= list_of_integers[cen - 1] and\
            list_of_integers[cen] >= list_of_integers[cen + 1]:
        return list_of_integers[cen]
    if cen > 0 and list_of_integers[cen] < list_of_integers[cen + 1]:
        return find_peak(list_of_integers[cen:])
    if cen > 0 and list_of_integers[cen] < list_of_integers[cen - 1]:
        return find_peak(list_of_integers[:cen])
