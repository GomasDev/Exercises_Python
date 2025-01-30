#Ejercicio 8. Crea un programa que dada la longitud de los dos catetos
# de un triángulo rectángulo obtenga la hipotenusa. Recuerda el teorema
# de Pitágoras → h2 = c12+c22 o lo que es lo mismo h = math.sqrt( c12+c22 ).
# Una vez creada comprueba que funciona.

import math


try:
    c1=float(input("Introduce el valor del cateto 1: "))
    c2=float(input("Introduce el valor del cateto 2: "))
except ValueError as error:
    print(f"ERROR: {error}")
else:
    h=math.sqrt(c1**2+c2**2)
    print(f"La hipotenusa es: {h:.2f}")