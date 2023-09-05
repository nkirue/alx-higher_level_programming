#!/usr/bin/python3
# 6-print_comb3.py

"""prints all possible different combinations of two digits

    01 and 10 are considered the same combination of the two digits 0 and 1
    """
for dig1 in range(0, 10):
    for dig2 in range(dig1 + 1, 10):
        if dig1 == 8 and dig2 == 9:
            print("{}{}".format(dig1, dig2))
        else:
            print("{}{}".format(dig1, dig2), end=", ")
