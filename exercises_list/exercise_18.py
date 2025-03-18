#Ejercicio 18. Escribe un programa que genere una lista con los n números
#pares comprendidos entre a y b. Los parámetros n, a y b son leídos desde
#teclado.
import random

n = int(input("Introduce el numero de numeros que quieres introducir: "))
a = int(input("Introduce el valor a, limite: "))
b = int(input("Introduce el valor b, limite: "))

list = []

for i in range(a, b):
    if i % 2 == 0 and len(list) <n:
        list.append(i)

print(list)
