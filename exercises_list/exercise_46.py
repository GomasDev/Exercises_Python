"""Ejercicio 46. Encuentra la suma de todos sus números.
 Hazlo primero sin usar sum() y luego usándolo"""

matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

suma = 0
for fila in matriz:
    for columna in fila:
        print(columna, end=' ')
        suma += columna
    print()

print("La suma es: ",suma)