#Ejercicio 6. Crea un programa que lea tres variables:
#inicio, fin y nVeces. Pudiendo ser inicio y fin números reales.
#El programa deberá crear <nVeces> números reales aleatorios
#entre <inicio> y <fin> redondeados a dos cifras decimales.


import random


try:
    inicio=float(input("Introduce el inicio: "))
    fin=float(input("Introduce el fin: "))
    nVeces=int(input("Introduce el numero de veces: "))
except ValueError as error:
    print(f"ERROR: {error}")
else:
    for i in range(nVeces):
        num=random.uniform(inicio,fin)
        print(round(num,2))