"""Ejercicio 47. Encuentra la fila y columna en la que se encuentra el número 5.
 Primero sin usar index() y luego usándolo"""

matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]



for i,fila in enumerate(matriz):
    for j, columna in enumerate(fila):
        if columna == 4:
            print("El numero 4 se encuentra en la fila: ",i+1 ,"en la columna: ",j+1)