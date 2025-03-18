"""Ejercicio 45. Crea una lista con 100 números pares
aleatorios entre 0 y 10."""


import random

numbers = [num for num in [random.randint(0,10) for num in range(1,101) ]if num % 2 == 0]

print(numbers)

#corregir