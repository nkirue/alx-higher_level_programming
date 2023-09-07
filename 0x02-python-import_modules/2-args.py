#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cl_arg = sys.argv
    num_args = len(cl_arg) - 1

    if num_args > 1:
        print("{} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, cl_arg[i]))

    elif num_args == 0:
        print("{} arguments.".format(num_args))

    else:
        print("{} argument:".format(num_args))
        print("{}: {}".format(num_args, cl_arg[1]))
