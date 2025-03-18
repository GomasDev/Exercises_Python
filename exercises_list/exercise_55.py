"""Ejercicio 55. Crea una función que reciba cuatro parámetros:
n → Número de filas
m → Número de columnas
a → Valor inicial
b → Valor final
La función deberá devolver una matriz de nXm elementos de números 
aleatorios entre a y b 
"""

import random


def imprimir_matriz(matriz):
    for linea in matriz:
        for columna in linea:
            print(columna, end=(" "))
        print()

def matriz(n, m, a, b):
    matriz_resultado = []

    for i in range(n):
        fila = []  # Una fila vacía
        for j in range(m):
            fila.append(random.randint(a, b))

        matriz_resultado.append(fila)
    return matriz_resultado

n = 4
m = 3
a = 1
b = 10

matriz_generada = matriz(n, m, a, b)
imprimir_matriz(matriz_generada)