#Ejercicio 1 (1 punto). Crea un programa que lea números hasta que la suma
# total de los números introducidos sea igual o mayor a 100. Al finalizar el
# programa mostrará por pantalla: a) la cantidad de números introducidos,
# b) la suma total, c) la media, d) el número mayor y e) el número menor.

cantidad=0
suma=0
nummax=0
nummin=0
while suma<100:
    num=int(input("Introduce un numero: "))
    if nummin==0:
        nummin=num
    if num>nummax:
        nummax=num
    if num<nummin:
        nummin=num
    suma = suma + num
    print(suma)
    cantidad += 1
media=suma/cantidad
print("La suma es: ",suma)
print("La media es: ",media)
print("La cantidad de numeros introducidos es: ",cantidad)
print("El numero mayor es: ",nummax)
print("El numero menor es: ",nummin)