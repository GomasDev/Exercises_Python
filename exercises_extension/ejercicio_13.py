#Crea una función que encuentre todas las palabras de un texto que           !¡!¡!¡
#empiecen por una determinada subcadena y el porcentaje, con respecto al total del
#texto, que representan dichas palabras. (string: texto, string: subcadena) => (string[]:
#palabras, int: porcentaje)

def porcentaje(texto, subcadena):
    texto_limpio=texto.lower()
    subcadena_limpia=subcadena.lower()
    palabras=texto_limpio.split()
    palabras_encontradas=[]
    count=0
    for p in palabras:
        
        if p.startswith(subcadena_limpia):
            palabras_encontradas.append(p)
    numero_encontradas=len(palabras_encontradas)
    numero_palabras=len(palabras)

    return ((numero_encontradas/numero_palabras)*100)

texto='Me gustan los melocotones y merendar platanos'
subcadena=input("Dime un prefijo para buscar la palabra: ")
print("Este es el porcentaje de veces que aparece las palabras con ese prefijo: ",porcentaje(texto,subcadena))