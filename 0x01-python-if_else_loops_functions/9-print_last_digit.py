#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = number % -10
        print("{:d}".format(-last), end="")
        return -last
    print("{:d}".format(number % 10), end="")
    return number % 10
