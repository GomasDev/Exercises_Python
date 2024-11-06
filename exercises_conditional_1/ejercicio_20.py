#Crea un programa que determine si tres longitudes de lados
#proporcionadas pueden formar un triángulo válido. La condición
#para que tres lados formen un triángulo es que la suma de las longitudes
#de cualesquiera dos lados debe ser mayor que el tercer lado.

lado1 = float(input("Inserta la longitud del lado 1: "))
lado2 = float(input("Inserta la longitud del lado 2: "))
lado3 = float(input("Inserta la longitud del lado 3: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print("El triángulo es válido")
else:
    print("El triángulo no es válido")