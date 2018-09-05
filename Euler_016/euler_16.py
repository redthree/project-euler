#! /usr/bin/python3


def powerSum(x, y):
    power = x ** y
    power_str = str(power)
    sum = 0
    for x in power_str:
        sum = sum + int(x)

    return sum

print(powerSum(2, 1000))
