"""Ejercicio 52. Halla el alumno cuya nota media sea la más baja"""
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

minima = 100
alumno_minima = ""

for linea in alumnos:
    nombre = linea[0]
    notas = linea[1:]

    media = statistics.mean(notas)

    if media < minima:
        minima = media
        alumno_minima = nombre


print(minima)
print(alumno_minima)
imprimir_matriz(alumnos)