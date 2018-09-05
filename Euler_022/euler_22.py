#! /usr/bin/python3


# List names in the file
names_list = []
with open('names.txt') as f:
    for line in f:
        names_list.extend([str(i) for i in line.replace('"', '').split(',')])

# Sort alphabetically 
names_list.sort()

#Alphabet
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def findInAbc(n):
    for position, item in enumerate(abc):
        if item == n:
            return int(position+1)
            break

resultado = 0

for position, name in enumerate(names_list):
    letters_sum = 0
    for letter in name:
        print(findInAbc(letter))

    # print(letters_sum * position)
