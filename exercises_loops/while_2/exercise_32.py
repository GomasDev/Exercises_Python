#Crea un programa que insertado un número n genere los n
#primeros términos de la sucesión de Fibonacci.
num=int(input("Introduce un numero: "))
a = b = 1
while a <= num:
    print(a)
    (a,b) = (b,a+b)