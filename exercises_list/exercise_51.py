"""Ejercicio 51. Halla la nota media de cada alumno"""
import statistics


def imprimirMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print("")


alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

suma = []

for fila in alumnos:
    nombre = fila[0]
    notas = fila[1:]

    media = statistics.mean(notas) #calcula la media automaticamente

    print("La nota media: ", media, "del nombre: ", nombre)

imprimirMatriz(alumnos)