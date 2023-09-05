#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """the numbers from 1 to 100 separated by a space.

    For multiples of three print Fizz instead of the 
    number and for multiples of five print Buzz.
    For multiples of both 3 and 5 print FizzBuzz
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
