#Ejercicio 16. Crea un programa con una lista que contenga el resultado de
#haber lanzado 10 veces una moneda al aire (cara o cruz).

import random

opciones=["cruz","cara"]
list=[]

for _ in range(10):
    list.append(random.choice(opciones))

print(list)