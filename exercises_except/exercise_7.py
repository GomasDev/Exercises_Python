#Ejercicio 7. Crea un programa que resuelva ecuaciones de 
# segundo grado a partir de los términos a, b y c. 
# El programa debe continuar hasta que el término a sea igual a 0.

import math


while True:
    try:
        a=int(input("Ingrese el valor de a: "))
        if a==0:
            print("Saliendo del programa.")
            break
        else:
            b=int(input("Ingrese el valor de b: "))
            c=int(input("Ingrese el valor de c: "))

    except ValueError as error:
        print(f"ERROR: {error}")


    else:
        discriminante=b**2-4*a*c
        if discriminante<0:
            print("No tiene solucion")
        else:
            raiz=math.sqrt(discriminante)
            x_1=-b+raiz/(2*a)
            x_2=-b-raiz/(2*a)
            print(f"Solucion 1: {x_1:.2f} y Solucion 2: {x_2:.2f}")