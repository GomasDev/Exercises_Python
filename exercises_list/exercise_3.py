#Ejercicio 3. Crea una lista con 10 números
# (los que quieras pero que no estén
#ordenados). Muestra por pantalla solo
# aquellos números que sean mayores al
#primero.

numeros = [3, 4, 2, 7, 10, 8, 15, 32, 12, 1]
primero = numeros[0]


for i in numeros:
    if i > primero:
        print(i)