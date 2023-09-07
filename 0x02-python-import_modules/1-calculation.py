#!/usr/bin/python3

if __name__ == "__main__":
    """prints the add,sub,mul, div of 10 and 5"""
    import calculator_1 as cal

    a = 10
    b = 5
    
    print("{} + {} = {}".format(a, b, cal.add(a, b)))
    print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    print("{} * {} = {}".format(a, b, csl.mul(a, b)))
    print("{} / {} = {}".format(a, b, cal.div(a, b)))
