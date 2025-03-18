"""Ejercicio 23. Crea un programa que permita insertar números naturales* en
una lista. Cada vez que insertes un número deberá mostrar la lista entera. Si
se inserta un número negativo deberá eliminar la primera aparición de su
análogo positivo de la lista, es decir si inserto -3 lo que significa es “elimina
el primer tres insertado”
* Números enteros entre 1 e infinito"""


lista = []

while True:
    num = int(input("Inserta un numero: "))

    if num < 0:
        for i in lista:
            if -num  == i:
                lista.remove(i)
    else:
        lista.append(num)
    print(lista)