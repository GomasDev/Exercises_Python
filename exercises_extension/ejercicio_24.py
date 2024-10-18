#Crea una función que determine si dos números son primos relativos.      ¡!¡!¡!¡!¡!
#(int: a, int: b) => (int[]: primos)
import math


def mcd(a,b):
    return math.gcd(a,b) #calcula directamente el mcd de dos valores, se importa con la libreria math


a=int(input("Introduce un valor: "))
b=int(input("Introduce un segundo valor: "))
if mcd(a,b)==1:
    print("Son primos relativos: ",a,b)
else:
    print("No son primos relativos: ",a,b)