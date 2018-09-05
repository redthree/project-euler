#! /usr/bin/python3

from math import factorial


def sumFactorial(num):
    factResult = factorial(num)
    numbers = list(map(int, str(factResult)))

    result = 0

    for x in numbers:
        result += x

    return result

print (sumFactorial(100))
