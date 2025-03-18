#Ejercicio 17. Crea un programa que lea números hasta que insertes un 0. Al
#terminar de leer números deberá mostrar por pantalla aquellos números
#insertados que sean superiores a la media.


list = []
media = 0
suma_num = 0

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    list.append(num)

suma_num = sum(list)
media = suma_num / len(list)
for num in list:
    if num>media:
        print(num)

print(list)