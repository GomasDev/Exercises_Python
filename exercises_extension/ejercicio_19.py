#Crea una función que sume los dígitos de un número. Ejemplo:    ¡!¡!¡!¡!
#sumaDigitos(245) = 2 + 4 + 5 = 11. (int: n) => (int: suma)


def sumaDigitos(num):
    suma=0
    for n in str(num):
        suma+=int(n)
    return suma


num=int(input("Introduce un numero: "))
print(sumaDigitos(num))