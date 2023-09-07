#!/usr/bin/python3

if __name__ == "__main__":
    """prints the add,sub,mul, div of 10 and 5"""
    import calculator_1 as calc

    a = 10
    b = 5
    
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, cslc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
