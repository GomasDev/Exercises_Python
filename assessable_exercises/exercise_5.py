"""Ejercicio 5 (1 punto). Crea una función que recibido un número entero muestre por pantalla los divisores de dichos número:

Usa la función para comprobar que funciona.
"""

def divisores(num: int):
    n=0
    while n<num:
        n+=1
        if num%n==0:
            print(n)

num=int(input("Introduce num opara calcular los divisores: "))
divisores(num)