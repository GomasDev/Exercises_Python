#Crea una función que cuenta cuantas veces aparece una subcadena en un texto            !!!!!!
#y el índice de inicio y fin de cada una de las instancias de la subcadena
#dentro del texto.
#(string: texto, string: subcadena) => (int: n_veces, [[int: inicio, int: fin]])

def num_palabra(texto, subcadena):
    texto_limpio = texto.lower()  # Convertimos el texto a minúsculas
    subcadena = subcadena.lower()
    indices = []  # Lista para almacenar los índices de inicio y fin
    n_veces = 0
    start = 0  #indice para iniciar

    while True:
        # Buscar la subcadena a partir del índice 'start'
        start = texto_limpio.find(subcadena, start) #buscar la primera aparición de una subcadena dentro de una cadena (string)
        
        if start == -1:
            # Si find() devuelve -1, significa que no hay más apariciones
            break
        
        # Añadimos el índice de inicio y el índice de fin a la lista
        indices.append([start, start + len(subcadena) - 1])  #append() en Python se usa para agregar un elemento al final de una lista.
        n_veces += 1
        
        # Mover el índice de inicio para la próxima búsqueda
        start += len(subcadena)
    
    return n_veces, indices

texto = 'Pepe le gusta otro nene que se llama pepe y tiene un primo que se llama pepe tmb'
subcadena = input("Introduce una palabra a buscar: ")
n_veces, indices = num_palabra(texto, subcadena)

print(f"El número de veces que aparece la palabra "+subcadena+" es: ",n_veces)
print("Índices de inicio y fin de cada instancia de la subcadena:")
for inicio, fin in indices:
    print(f"Inicio: ",inicio,", Fin: ",fin)