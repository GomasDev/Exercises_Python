#Crea un programa que lea números hasta que se introduzca un
#0. El programa deberá calcular la media aritmética de todos los números
#insertados, el número máximo y el número mínimo.

num=int(input("Introduce un numero: "))
suma=0
count=-1
nummax=num
nummin=num
while num!=0:
    num=int(input("Introduce un numero: "))
    if num!=0:
        if num>nummax:
            nummax=num
        if num<nummin:
            nummin=num
    suma=suma+num
    count=count+1
media=suma/count
print("La media aritmetica es: ",media)
print("El numero maximo es: ",nummax)
print("El numero minimo es: ",nummin)