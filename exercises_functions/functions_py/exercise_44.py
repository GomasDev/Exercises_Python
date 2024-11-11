#Crea un programa que lea un número real y después un entero.
#El programa deberá devolver el número real introducido redondeado al
#número de cifras decimales especificado por el número entero. El programa
#deberá continuar hasta que el usuario inserte un 0 como número a
#redondear .

numReal=float(input("Enter a real number: "))
numEnt=int(input("Enter a number: "))

print(round(numReal,numEnt))