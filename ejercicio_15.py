#Crear un programa en el que el usuario elegirá una figura geométrica:
#triángulo, rectángulo o circunferencia. El programa deberá calcular
#el área de dicha figura geométrica.
import math

figura=input("Elige figura geometrica: (triangulo, rectangulo o circunfrencia)")
figura_nueva=figura.lower()

if figura_nueva=="triangulo":
    base=float(input("Introduce la base del triangulo: "))
    altura=float(input("Introduce la altura del triangulo: "))
    area=(base*altura)/2
    print("El area del triangulo es: ",area)
elif figura_nueva=="rectangulo":
    base=float(input("Introduce la base del rectangulo: "))
    altura=float(input("Introduce la altura del rectangulo: "))
    area=(base*altura)
    print("El area del ractangulo es: ",area)
elif figura_nueva=="circunferencia":
    radio=float(input("Introduce el radio de la circunferencia: "))
    area=(math.pi*radio**2)
    print("El area de la circunferencia es: ",area)
else:
    print("No has elegido una opcion correcta")