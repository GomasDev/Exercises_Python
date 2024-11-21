#Ejercicio 3. Crea un programa que lea números hasta que
# introduzcas un número repetido.

numRepetido=[]
while True:
    num=int(input("Introduce numero: "))
    if num in numRepetido:
        print("Numero repetido")
        break
    numRepetido.append(num)