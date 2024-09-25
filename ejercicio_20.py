#Crea una función que calcule el máximo común divisor de dos          ¡!¡!¡!¡¡!¡!
#números naturales. (int: a, int: b) => (int: mcd)

import math


def mcd(a,b):
    return math.gcd(a,b) #calcula directamente el mcd de dos valores, se importa con la libreria math


a=int(input("Introduce un valor: "))
b=int(input("Introduce un segundo valor: "))

print("Minimo comun divisor es: ",mcd(a,b))