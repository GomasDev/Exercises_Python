"""Ejercicio 54. Halla la nota media de toda la clase"""
import statistics


def imprimir_matriz(matriz):
    for linea in matriz:
        for columna in linea:
            print(columna, end=" ")
        print(" ")

alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

suma_nota = 0
n_alumnos = len(alumnos)

for linea in alumnos:
    notas = linea[1:]

    suma_nota += sum(notas)/3

nota_media = suma_nota / n_alumnos
print(nota_media)

imprimir_matriz(alumnos)