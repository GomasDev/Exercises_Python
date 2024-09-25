#Crea una función que determine que palabras de un texto tiene una
#longitud mayor a una dada. (string: texto, int: longitud) => (string[]: palabras)

def longitud_mayor(texto,longitud):
    texto_limpio=texto.lower()
    palabras=texto_limpio.split()
    palabras_filtradas=[]
    longitud=int(longitud)

    for p in palabras:
        if len(p)>=longitud:
            palabras_filtradas.append(p)
    return palabras_filtradas


longitud_dada=input("Dime una longitud para buscar palabras: ")
texto=("Hola me llamo perry el ornitorrinco")
palabras_mayores=longitud_mayor(texto,longitud_dada)
print(palabras_mayores)