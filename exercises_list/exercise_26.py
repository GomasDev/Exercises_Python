"""Ejercicio 26. Crea un programa que inserte números en una lista. Si el
número ya existe en la lista NO debe volver a introducirlo, de tal forma que
la lista no contenga número repetidos:"""


lista_num = []

while True:
    num = int(input("Ingrese un numero: "))

    if lista_num.count(num) < 1:
        lista_num.append(num)

    print(lista_num)
    if num == 0:
        break
print(lista_num)