"""Ejercicio 53. Halla los alumnos que tengan
al menos una asignatura suspensa"""

def imprimir_matriz(matriz):
    for linea in matriz:
        for columna in linea:
            print(columna, end=" ")
        print("")

alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

suspensos = []

for linea in alumnos:
    nombre = linea[0]
    notas = linea[1:]

    for nota in notas:
        if nota < 5:
            suspensos.append(nombre)
        break

print(suspensos)
imprimir_matriz(alumnos)