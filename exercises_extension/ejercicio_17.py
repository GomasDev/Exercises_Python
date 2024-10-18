#Crea una función que calcula el área de triángulo o cuadrado dados su
#base y altura o el de una circunferencia dado su radio. (string: figura, int[]: longitudes)
#=> (int: área)

import math


def calcular_area(figura,longitudes):
    if figura.lower()=="circunferencia":
        if len(longitudes) == 1:
            radio = longitudes[0]
            area = math.pi * radio ** 2
        else:
            return "Error: Una circunferencia necesita solo el radio."
    
    elif figura.lower()=="cuadrado":
        if len(longitudes) == 1:
            lado = longitudes[0]
            area = lado * lado
        else:
            return "Error: Un cuadrado necesita solo un lado."
    elif figura.lower()=="triangulo":
        if len(longitudes) == 2:
            base = longitudes[0]
            altura = longitudes[1]
            area = (base * altura) / 2
        else:
            return "Error: Un triángulo necesita exactamente base y altura."
    return area
    
figura=input("Introduce la figura: ")
longitudes=list(map(float,input("Introduce las longitudes: ").split())) #introduces valores en string y separamos en listas con split() y luego convertimos a float todos los valores
print("El area de la figura es: ",calcular_area(figura,longitudes))