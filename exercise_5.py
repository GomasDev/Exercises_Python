#Ejercicio 5. Sin usar listas crea un programa que lea 10 números.
# El programa deberá imprimir por pantalla los tres números más grandes introducidos.

num=int(input("Enter a number: "))
nummayor1=nummayor2=nummayor3=0
for i in range(10):
    num=int(input("Enter a number: "))
    if num>nummayor1:
        nummayor3=nummayor2
        nummayor2=nummayor1
        nummayor1=num
    elif num>nummayor2:
        nummayor3=nummayor2
        nummayor2=num
    elif num>nummayor3:
        nummayor3=num
print("El numero mayor es: ",nummayor1)
print("El segundo numero mayor es: ",nummayor2)
print("El tercer numero mayor es: ",nummayor3)