#! /usr/bin/python3

# Get divisors
def d(n):
    result = 0
    for x in range(1, n-1):
        if n % x == 0:
            result += x

    return result

# Exists in the list??
def exists(num, listado):
    cont = 0
    resultado = False
    for x in listado:
        if x[0] == num or x[1] == num:
            resultado = True
            break
        cont += 1

    return resultado

# Get amicables
def amicables(n):
    listado = []

    while n > 0:
        x = d(n)
        y = d(d(n))
        if n == y:
            if (x != y and exists(x, listado) is False and
                exists(y, listado) is False):
                listado.append([x, y])
        n -= 1

    return listado


result = 0
amicables_numbers = amicables(10000)

print(amicables_numbers)

for x in amicables_numbers:
    result += x[0] + x[1]

print(result)
