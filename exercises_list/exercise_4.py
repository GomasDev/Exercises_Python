#Ejercicio 4. Crea una lista con 10 números (los que quieras).
# Muestra por pantalla la media de dichos números

numeros = [3, 4, 2, 7, 10, 8, 15, 32, 12, 1]
media = 0
suma=0

for numero in numeros:
    suma += numero

media = suma / len(numeros)
print(media)