#! C:/Python33/

# -- EULER 12 --

# Cantidad de divisores
# def divisores(x):
#     n, i = 0, 2
#     while i < x and i <= x/2:
#         if x % i == 0:
#             n += 1
#         i += 1
#     n += 2
#     return n

def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

# Numeros Triangulares
def triangulares():
    x = 1
    suma = 0
    div = 0
    encontrado = False
    
    while encontrado != True:
        for i in range(1, x):
            suma = suma + i
        
        if len(factors(suma)) > 500:
            print("Encontrado!!!")
            encontrado = True

        print(str(suma) + ": " + str(len(factors(suma))))

        suma = 0
        x += 1
        
    return suma


print(triangulares())