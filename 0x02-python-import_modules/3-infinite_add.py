#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    cl_arg = len(sys.argv) - 1

    total = 0
    for i in range(cl_arg):
        total =  total + int(sys.argv[i + 1])
    print("{}".format(total))
