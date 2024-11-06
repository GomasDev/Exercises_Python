#Crea un programa que dado un número calcule su factorial.
#Nota: no uses la función factorial ya programada por Python, la gracia del
#ejercicio es que lo calcules con bucles.

num=int(input("Introduce un numero para calcular su factorial: "))
n=1
factorial=1
while n<=num:
    factorial=factorial*n
    n=n+1
print("Factorial es: ",factorial)