#Crea un programa que convierta temperaturas.
#El usuario debe ingresar una temperatura y
#la escala original (Celsius o Fahrenheit) y el programa la convertirá a la otra escala.

temperatura=float(input("Introduce una temperatura: "))
escala=input("Introduce la escala: (celsius(c) o Fahrenheit(f))")


escala_nueva=escala.lower()

if escala_nueva=="c":
    temperatura_convertida = (temperatura * 9/5) + 32
    print("La temperatura es fahrenheit es: ",temperatura_convertida)
elif escala_nueva=="f":
    temperatura_convertida = (temperatura - 32) * 5/9
    print("La temperatura es celsius es: ",temperatura_convertida)
else:
    print("Escala no reconocida.")