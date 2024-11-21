#Ejercicio 2. Crea un programa que lea 10 números.
# El programa deberá imprimir por pantalla los dos
# números más grandes introducidos.

nummayor1=nummayor2=0
for _ in range(10):
    num=int(input("Enter a number: "))
    if num>nummayor1:
        nummayor2=nummayor1
        nummayor1=num
    elif num>nummayor2:
        nummayor2=num

print("El numero mayor es: ",nummayor1)
print("El segundo numero mayor es: ",nummayor2)