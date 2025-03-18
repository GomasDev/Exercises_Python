"""Ejercicio 44. Crea una lista con 100 números aleatorios entre 0 y 10."""
import random

numbers = [random.randint(0,10) for num in range(1,101)]

print(numbers)