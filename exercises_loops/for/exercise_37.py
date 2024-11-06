#Crea un programa que dado un número calcule su factorial.

num=int(input("Introduce un numero: "))
factorial=1
for n in range(1,num+1):
    factorial=factorial*n
print(factorial)