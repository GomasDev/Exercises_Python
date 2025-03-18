"""Ejercicio 48. Transforma los números negativos a positivos.

"""
def imprrime_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print()


matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

for fila in matriz:
    for j, columna in enumerate(fila):
        if columna < 0:
            fila[j] *= -1

imprrime_matriz(matriz)