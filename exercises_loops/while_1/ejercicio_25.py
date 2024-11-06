#Crea una variable de nombre ‘numSecreto’ que
#  contenga un número entre 0 y 100 (el que tu quieras).
#  El programa debe pedir al usuario que intente adivinar el número.
#  Una vez que el usuario inserte el número el programa le dirá si ha
#  acertado o si ha fallado le dirá si el número secreto es mayor o
#  menor que el introducido.
#  Cuando el usuario acierte el número el programa le dirá cuántos intentos ha empleado

numSecreto=56
num=int(input("Intenta adivinar el numero: "))
count=1
while num!=numSecreto:
    print("Has fallado.")
    count+=1
    if num<numSecreto:
        print("El numero es menor")
    else:
        print("El numero es mayor")
    num=int(input("Intenta adivinar el numero: "))
print("Has aertado el numero")
print("Ha habido ",count,"intentos")