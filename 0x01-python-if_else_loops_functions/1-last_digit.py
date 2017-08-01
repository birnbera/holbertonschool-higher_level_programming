#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = number % -10 if number < 0 else number % 10
print("Last digit of {:d} is {:d}".format(number, lastdig), end=" ")
if lastdig == 0:
    print("and is 0")
elif lastdig > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
