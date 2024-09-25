#Crea una función que encuentra la palabra de mayor
# longitud en una  cadena texto y la longitud de la misma.
#(string: texto) => (string: palabra, int: longitud)

def palabra_mayor(texto):
    lista_palabra=texto.split()  #divide la cadena en distintas palabras      list()---->divide en letras
    mayor=''
    tamaño=0
    for palabra in lista_palabra:
        if len(palabra)>tamaño:
            mayor=palabra
            tamaño=len(palabra)
    return mayor,tamaño

texto='hola me llamo rafa'
palabra,tamaño=palabra_mayor(texto)
print("La palabra es "+palabra+" y su tamaño es ",tamaño)