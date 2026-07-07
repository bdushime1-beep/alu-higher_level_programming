#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10

if last_digit < 0:
    last_digit += 10

# adjust sign to match number's sign for display
display_digit = number % 10

if display_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(
        number, display_digit))
elif display_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, display_digit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(
        number, display_digit))
