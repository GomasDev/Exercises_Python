"""Ejercicio 6. Crea la función suma_matrices(m1:list, m2:list) que dadas dos
matrices m1 y m2 devuelva su suma. Tutorial de cómo sumar matrices."""

def suma_matrices(m1, m2):
    # Comprobamos que ambas matrices tengan las mismas dimensiones
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")

    resultado = []
    for i in range(len(m1)):
        fila_resultado = []
        for j in range(len(m1[0])):
            fila_resultado.append(m1[i][j] + m2[i][j])
        resultado.append(fila_resultado)

    return resultado


# ejemplos de uso
matriz_1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_2 = [
    [6, 5, 4],
    [3, 2, 1]
]

print(suma_matrices(matriz_1, matriz_2))