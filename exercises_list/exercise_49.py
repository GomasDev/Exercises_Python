"""Ejercicio 49. Encuentra el animal con más letras de la lista"""



def imprimir_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end = " ")
        print()

matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

mayor = matriz[0][0]

for fila in matriz:
    for columna in fila:
        if len(columna) > len(mayor):
            mayor = columna

print("El mayor es: ", mayor)

imprimir_matriz(matriz)