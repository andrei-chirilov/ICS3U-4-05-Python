#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program adds positive integers

import random


def main():
    counter = 0
    integer = 0
    answer = 0
    exception = False

    try:
        number = int(input("How many numbers are you going to add?: "))
        for counter in range(number):
            integer = int(input("Enter number you are going to add: "))
            if integer < 0:
                continue
            else:
                answer = answer + integer
    except ValueError:
        exception = True
        print("Not a valid input")

    if exception is False:
        print("Sum of positive integers is " + str(answer))


if __name__ == "__main__":
    main()
