#Crea una función que determina si una letra es una vocal. (string: letras)
#=> (boolean: es_vocal)

def es_vocal(letra):
    letra_limpia=letra.lower()
    vocales=["a","e","i","o","u"]
    if letra_limpia in vocales:
        return True
    return False
letra=input("Introduce una vocal: ")
print(es_vocal(letra))