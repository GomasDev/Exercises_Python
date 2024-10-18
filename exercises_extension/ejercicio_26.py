#Crea una función que calcule todos los números capicúas de un intervalo
#[a, b). (int: a, int: b) => (int[]: nums)

def capicuas(a,b):
    lista=[]
    for c in range(a,b):
        if str(c)==str(c)[::-1]:
            lista.append(c)
    return lista
a=int(input("Introduce primer valor para un intervalo: "))
b=int(input("Introduce un segundo valor para el intervalo: "))
print(capicuas(a,b))