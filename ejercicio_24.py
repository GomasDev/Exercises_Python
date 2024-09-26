#Crea una función que determine si un número dado es capicúa. (int: n)
#=> (boolean: es_capicua)

def capicua(num):
    if num==num[::-1]:
        return True
    return False

num=input("Introduce un numero: ")
print(capicua(num))