#! /usr/bin/python3
import math


def permutation(a, b):
    return math.factorial(a) / math.factorial(b)


def combination(a, b):
    return permutation(a, b) / math.factorial(b)


print(combination(40, 20))
