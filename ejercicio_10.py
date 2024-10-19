# Crea un programa que dado el peso de un coche determine si es un coche ligero, medio o pesado.
#  Diremos que un coche es ligero si su peso es menor a una tonelada, será de peso medio si pesaç
#  entre 1 y 2 toneladas y si pesa más entonces diremos que un coche pesado.

peso_coche=float(input("Introduce el peso del coche: "))
if peso_coche<=1:
    print("El coche es ligero")
elif peso_coche<=2:
    print("El coche tiene peso medio")
else:
    print("El coche es pesado")