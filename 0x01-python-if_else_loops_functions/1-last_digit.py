#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, end=" ")
num = (abs(number) % 10)
if number >= 5:
    print("is {} and is greater than 5".format(num))
elif number == 0:
    print("is {} and is 0".format(num))
else:
    print("is -{} and is less than 6 and not 0".format(num))
