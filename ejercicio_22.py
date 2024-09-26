#Crea una función que encuentra todos los números primos en un
#intervalo [a, b). (int: a, int: b) => (int[]: primos)

def primo(num):
    for n in range (2,num):
        if num%n==0:
            return False
    return True

def primos(a,b):
    primos=[]
    for n in range (a,b):
        if primo(n):
            primos.append(n)
    return primos

a=int(input("Introduce un numero para el rango de numeros primos: "))
b=int(input("Introduce un segundo numero para el rango de numeros primos: "))
print(primos(a,b))