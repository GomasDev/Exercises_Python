#Ejercicio 2 (1 punto). Crea un programa que muestre por pantalla 10 números
# aleatorios entre 20 y 40. Además deberá mostrar el porcentaje de número
# pares generados y el de números impares

import random

i=0
pares=0
impares=0
while i<10:
   i+=1
   num=random.randint(20,40)
   if num%2==0:
       pares+=1
   else:
       impares+=1
   print(num)
print("La cantidad de numeros pares es: ",pares)
print("El porcentaje es: ",pares*100/10,"%")
print("La cantidad de numeros impares es: ",impares)
print("El porcentaje es: ",impares*100/10,"%")