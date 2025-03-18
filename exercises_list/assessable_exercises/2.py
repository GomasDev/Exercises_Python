"""Ejercicio 2. Crea una función que dadas una lista de números y un número n
determine si todos los números de la lista son mayores o iguales a n. La
función deberá devolver True o False."""



def mayores(lista, numero):
    for num in lista:
        if num < numero:
            return False
    return True


# Ejemplo de uso
numeros = [10, 15, 20, 25, 30]
n = 2

resultado = mayores(numeros, n)
print(resultado)