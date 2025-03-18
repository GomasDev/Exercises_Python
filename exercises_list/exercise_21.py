#Ejercicio 21. Crea un programa que inserte números en una lista hasta que
#insertes el número 0 para terminar. Los números deberán estar ordenados de
#menor a mayo. Prohibido utilizar el método .sort().
lista_num = []

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break

    if not lista_num:  # Si la lista está vacía,añadimos el número
        lista_num.append(num)
    else:
        for i in range(len(lista_num)):
            if num < lista_num[i]:  # Encuentra la posición correcta
                lista_num.insert(i, num)
                break
        else:
            lista_num.append(num)  # Si no encontró un lugar, lo añade al final

print("La lista ordenada:", lista_num)

