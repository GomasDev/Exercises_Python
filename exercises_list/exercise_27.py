"""Ejercicio 27. Crea una lista con 1000 números aleatorios entre 1 y 100.
Encuentra el número que MÁS veces se repite."""
import random

lista = []
mas_repetido = None
max_count=0

while len(lista) < 1000:
    lista.append(random.randint(1, 100))

    for i in lista:
        ocurrencia = lista.count(i)
        if ocurrencia > max_count:
            max_count = ocurrencia
            mas_repetido = i

print("El numero que mas veces se repite es: ", mas_repetido, " y se repite: ", max_count)