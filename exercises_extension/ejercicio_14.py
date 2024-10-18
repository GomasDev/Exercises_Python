#Crea una función que encuentre todas las palabras de un texto que        !¡!¡!¡
#empiecen por una subcadena y que NO termine por otra subcadena. (string: texto,
#string: subcadena1, string: subcadena2) => (string[]: palabras)

def palabras_encontradas(texto, subcadena1,subcadena2):
    texto_limpio=texto.lower()
    subcadena1_limpia=subcadena1.lower()
    subcadena2_limpia=subcadena2.lower()
    palabras=texto_limpio.split()
    palabras_encontradas=[]
    count=0
    for p in palabras:
        
        if p.startswith(subcadena1_limpia) and p.endswith(subcadena2_limpia)==False:
            palabras_encontradas.append(p)

    return palabras_encontradas

texto='Me gustan los melocotones y merendar platanos como a los monos'
subcadena1=input("Dime un prefijo para buscar la palabra: ")
subcadena2=input("Dime un sufijo para buscar: ")
print("Estas son las palabras encontradas: ",palabras_encontradas(texto,subcadena1,subcadena2))