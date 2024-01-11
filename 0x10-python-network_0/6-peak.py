#!/usr/bin/python3
"""
Module for finding a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers (list): List of unsorted integers

    Returns:
    - int: A peak element from the list
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Calculate the cendle index
    cen = len(list_of_integers) // 2

    # Compare the cendle element with its neighbors
    if (cen == 0 or list_of_integers[cen] >= list_of_integers[cen - 1]) and \
       (cen == len(list_of_integers) - 1 or list_of_integers[cen] >= list_of_integers[cen + 1]):
        return list_of_integers[cen]

    # If the cendle element is not a peak, recurse on the side with the larger neighbor
    if cen > 0 and list_of_integers[cen - 1] > list_of_integers[cen]:
        return find_peak(list_of_integers[:cen])
    else:
        return find_peak(list_of_integers[cen + 1:])
