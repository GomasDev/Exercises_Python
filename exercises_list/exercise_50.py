"""Ejercicio 50. Encuentra el número de animales que empiezan por vocal
"""

def imprimir_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print("")


matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

vocales = "AEIOUaeiou"
contador = 0

imprimir_matriz(matriz)

for fila in matriz:
    for columna in fila:
        if columna[0] in vocales:
            contador +=1

print("El numero es: ", contador)