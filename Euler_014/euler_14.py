#! /usr/bin/python3


def collatz(x):
    arr = []
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = (3 * x) + 1
        arr.append(x)

    return len(arr)

start = 1000000
max_length = 0
winner = 0

while start > 0:
    collatz_length = collatz(start)
    if collatz_length > max_length:
        max_length = collatz_length
        winner = start
    start -= 1

print(winner)
