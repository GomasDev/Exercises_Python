#Crea un programa que te pida dos números y que te muestre
#por pantalla todos los números que hay entre el menor de los números
#introducidos y el mayor .

num=int(input("Introduce un numero: "))
num2=int(input("Introduce otro numero: "))

nummin=0
nummax=0

if num<num2:
    nummin=num
    nummax=num2

for n in range (nummin,nummax):
    print(n)

