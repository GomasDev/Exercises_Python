"""
Ejercicio 7 (1 punto). Crea un programa que primero lea una letra y luego lea
palabras hasta que introduzcas la palabra ‘fin’. El programa deberá mostrar la
cantidad de veces que dicha letra aparece en las palabras introducidas
(no tener en cuenta la palabra ‘fin’)."""

letra=input("Introduzca la letra: ")
palabra=None
count=0

while palabra!="fin":
    palabra = input("Introduce una palabra: ")
    if palabra!="fin":
        for n in palabra:
            if letra==n:
                count += 1

print("La cantidad es: ",count)