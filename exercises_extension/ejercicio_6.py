#Crea una función que cuenta cuantas veces aparece una letra en un texto.
#(string: texto, string: letra) => (int: n_veces)

def num_letra(texto,letra):
    texto_limpio=texto.lower()
    letras=list(texto_limpio)
    n_veces=0
    for l in letras:
        if l==letra:
            n_veces+=1
    return n_veces

letra=str(input("Dime una letra que buscas: "))
texto='Hola me llamo juan'
print(num_letra(texto,letra))