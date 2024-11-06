#Crea un programa que dado un número calcule si es primo o no.

num=int(input("Introduce un numero para saber si es primo: "))
primo=True
if num<2:
    primo=False
else :
    for n in range(2,num):
        if num%n==0:
            primo=False
            break

if primo==True:
    print("Es un numero primo")
else:
    print("No es numero primo")