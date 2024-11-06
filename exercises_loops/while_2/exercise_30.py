#Crea un programa que dado un número te muestre la tabla de
#multiplicar de dicho número (no uses el bucle for, limítate a usar while)


num=int(input("Introduce un numero: "))
print("TABLA DEL ",num)
n=-1
while n<10:
    n=n+1
    producto=num*(n)
    print(producto)