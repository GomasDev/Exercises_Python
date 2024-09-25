#Crea una función que pone en mayúscula la primera letra de cada
#palabra de un texto. (string: texto) => (string: texto)

#title() convierte la primera letra de cada palabra de una cadena a mayúsculas. Se llama formatoa titulo

def letra_mayus(texto):
    texto_limpio=texto.lower()
    return (texto_limpio.title())

texto=("hola me llamo rafa")
print(letra_mayus(texto))