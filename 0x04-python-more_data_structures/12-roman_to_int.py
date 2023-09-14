#!/usr/bin/python3
def to_sub(listnum):
    tosub = 0
    maximum_list = max(listnum)

    for x in listnum:
        if maximum_list > x:
            tosub += x

    return (maximum_list - tosub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(romn.keys())

    nom = 0
    lastrom = 0
    listnum = [0]

    for chr in roman_string:
        for rnum in list_keys:
            if rnum == chr:
                if romn.get(chr) <= lastrom:
                    nom += to_sub(listnum)
                    listnum = [romn.get(chr)]
                else:
                    listnum.append(romn.get(chr))

                lastrom = romn.get(chr)

    nom += to_sub(listnum)

    return (nom)
