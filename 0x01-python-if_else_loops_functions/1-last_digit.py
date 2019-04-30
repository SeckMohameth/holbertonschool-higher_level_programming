#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastNumber = (number * -1) % -10

else: lastNumber = number % 10

if lastNumber > 5:
    print("Last digit of {} is {} and is\
 greater than 5".format(number, lastNumber))
elif lastNumber == 0:
    print("Last digit of {} is {} and is 0".format(number, lastNumber))
elif lastNumber < 6 and number != 0:
    print("Last digit of {} is {} and is less than\
 6 and not 0".format(number, lastNumber))
