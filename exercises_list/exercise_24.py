"""Ejercicio 24. Crea un programa que inserte números en una lista hasta
introducir el número 0. A continuación deberá mostrar en pantalla todos los
números introducidos en orden inverso, es decir primero el último número
introducido."""


lista = []
lista_reversa = []

while True:
    num=int(input("Introduce numero: "))
    if num == 0:
        break
    lista.append(num)

for i in range(len(lista)):
    lista_reversa.append(lista.pop())

print(lista_reversa)