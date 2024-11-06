#Crea un programa que dado un caracter, una base y una altura
#te dibuje un rectángulo a partir de los datos introducidos.

char=input("Introduce un caracter: ")
base=int(input("Introduce una base: "))
altura=int(input("Introduce la altura: "))

linea = char
i = 1
while i < base:
    linea = linea + char
    i = i + 1

i = 0
while i < altura:
    print(linea)
    i = i + 1