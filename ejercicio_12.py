#Crea una función que cambie todas las ocurrencias de una letra dentro
#de un texto por otra letra. (string: texto, string: letra1, string: letra2) => (string: texto)

def sustituir_letra(texto,letra1,letra2):
    texto_limpio=texto.lower()
    nuevo_texto=texto_limpio.replace(letra1,letra2)
    return nuevo_texto

texto=("Hola me llamo Rafa")
letra1=input("Dime letra a sustituir: ")
letra2=input("Que letra quieres poner: ")
print(sustituir_letra(texto,letra1,letra2))