"""Ejercicio 4. Crea una función que reciba por parámetro una matriz. La
función deberá devolver una lista de dos elementos: el primero de ellos con el
número de filas de la matriz y el segundo con el número de columnas de la
matriz. No hagas comprobaciones de que lo que le entra sea o no una matriz,
supón que siempre recibirá por parámetro una matriz válida."""

def dimensiones_matriz(matriz):
    # El número de filas será simplemente el tamaño de la lista de la matriz
    filas = len(matriz)

    # El número de columnas será el tamaño de la primera fila
    columnas = len(matriz[0]) if filas > 0 else 0

    return [filas, columnas]


# Ejemplos de uso
matriz_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(dimensiones_matriz(matriz_1))

matriz_2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(dimensiones_matriz(matriz_2))

matriz_3 = [
    [1, 2, 3]
]
print(dimensiones_matriz(matriz_3))

