#Crea una función que cuenta cuantas veces aparece una subcadena en un texto.
# (string: texto, string: subcadena) => (int: n_veces)

def num_palabra(texto,subcadena):
    texto_limpio=texto.lower()
    subcadena=subcadena.lower()
    n_veces=0
    palabra=texto_limpio.split() #divide la cadena en distintas palabras
    for p in palabra:
        if p==subcadena:
            n_veces+=1
    return n_veces

texto='Pepe le gusta otro nene que se llama pepe y tiene un primo que se llama pepe tmb'
subcadena=str(input("Introduce un palabra a buscar: "))
print("El numero de veces que aparece esa palabra es: ",num_palabra(texto,subcadena))