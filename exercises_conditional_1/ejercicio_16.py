#Crea un programa que solicite al usuario la longitud de los tres lados de un triángulo y determine el tipo de triángulo:
#equilátero (todos los lados iguales), isósceles (dos lados iguales), escaleno (todos los lados diferentes).

lad1=float(input("Introduce el primer lado del triangulo: "))
lad2=float(input("Introduce el segundo lado del triangulo: "))
lad3=float(input("Introduce el tercero lado del triangulo: "))

if lad1==lad2==lad3:
    print("El triangulo es equilatero.")
elif lad1==lad2 or lad2==lad3 or lad1==lad3:
    print("El triangulo es isosceles.")
else:
    print("El triangulo es escaleno")