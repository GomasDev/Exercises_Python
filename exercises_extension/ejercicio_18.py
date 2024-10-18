#Crea una función que calcula el número de múltiplos de un número en un
#intervalo [a, b). (int: multiplicador, int: inicio, int: fin) => (int[]: múltiplos)

def multiplos(multiplicador,inicio,fin):
    list_multiplos=[]
    for n in range(inicio,fin):
        if n%multiplicador==0:
            list_multiplos.append(n)
    return list_multiplos

multiplicador=int(input("Introduce el valor al que le quieres caluclar los multiplos: "))
inicio=int(input("Introduce el inicio del rango a buscar: "))
fin=int(input("Introduce el final del rango a buscar: "))
print("Los multiplos del numero dado en ese rango son: \n")
print(multiplos(multiplicador,inicio,fin))