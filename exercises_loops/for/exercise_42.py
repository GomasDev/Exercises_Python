#Crea un programa que dado un texto cuente el número de
#vocales que tiene (independientemente de si están en minúscula o
#mayúscula)

texto = input("Introduce un texto: ")
nVocales = 0
for caracter in texto:
    if caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U" or caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        nVocales = nVocales + 1

print(nVocales)