#!/usr/bin/python3
def number_keys(a_dictionary):
    nom = 0
    listkeys = list(a_dictionary.keys())

    for x in listkeys:
        nom += 1

    return (nom)
