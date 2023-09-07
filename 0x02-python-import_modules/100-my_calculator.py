#!/usr/bin/python3
if __name__ == "__main__":
    """basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div 
    import sys
    no_arg = len(sys.argv) - 1	

    if no_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    output = operator[sys.argv[2]](a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, output ))
