#! /usr/bin/python3


def numberToWord(x):
    words = ""
    basic = ["", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen"]
    if x > 0:
        if x >= 100:
            y = x % 100
        else:
            y = x
        if y > 0 and y < 10:
            words = basic[y]
        if y > 9 and y < 20:
            words = tens[y % 10]
        if y > 19 and y < 30:
            words = "twenty{0}".format(basic[y % 10])
        if y > 29 and y < 40:
            words = "thirty{0}".format(basic[y % 10])
        if y > 39 and y < 50:
            words = "forty{0}".format(basic[y % 10])
        if y > 49 and y < 60:
            words = "fifty{0}".format(basic[y % 10])
        if y > 59 and y < 70:
            words = "sixty{0}".format(basic[y % 10])
        if y > 69 and y < 80:
            words = "seventy{0}".format(basic[y % 10])
        if y > 79 and y < 90:
            words = "eighty{0}".format(basic[y % 10])
        if y > 89 and y < 100:
            words = "ninety{0}".format(basic[y % 10])

    if x >= 100 and x < 200:
        if x == 100:
            words = "onehundred"
        else:
            words = "onehundredand" + words
    if x >= 200 and x < 300:
        if x == 200:
            words = "twohundred"
        else:
            words = "twohundredand" + words
    if x >= 300 and x < 400:
        if x == 300:
            words = "threehundred"
        else:
            words = "threehundredand" + words
    if x >= 400 and x < 500:
        if x == 400:
            words = "fourhundred"
        else:
            words = "fourhundredand" + words
    if x >= 500 and x < 600:
        if x == 500:
            words = "fivehundred"
        else:
            words = "fivehundredand" + words
    if x >= 600 and x < 700:
        if x == 600:
            words = "sixhundred"
        else:
            words = "sixhundredand" + words
    if x >= 700 and x < 800:
        if x == 700:
            words = "sevenhundred"
        else:
            words = "sevenhundredand" + words
    if x >= 800 and x < 900:
        if x == 800:
            words = "eighthundred"
        else:
            words = "eighthundredand" + words
    if x >= 900 and x < 1000:
        if x == 900:
            words = "ninehundred"
        else:
            words = "ninehundredand" + words
    if x == 1000:
        words = "onethousand"

    return words

sum = 0

for x in xrange(1, 1001):
    print(numberToWord(x))
    sum = sum + len(numberToWord(x))

print(sum)
