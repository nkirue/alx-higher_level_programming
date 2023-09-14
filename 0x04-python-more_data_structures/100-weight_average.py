#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    nom = 0
    don = 0

    for x in my_list:
        nom += x[0] * x[1]
        don += x[1]

    return (nom / don)
