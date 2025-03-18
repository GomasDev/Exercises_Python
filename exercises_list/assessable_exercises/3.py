"""Ejercicio 3. Dada una lista con 2^n elementos, por ejemplo:
Crear una función que imprima por pantalla el emparejamiento aleatorio de
todos los elementos de la lista, por ejemplo para la anterior:
NOTA: USAR SOLO FUNCIONES ESTUDIADAS
NOTA2: la lista original no debe ser modificada
"""
import random


def emparejamiento_aleatorio(lista):
    lista_copia = lista.copy()  #copiamos lista pa no modificarla
    emparejamientos = []

    while lista_copia:  # Mientras haya jugadores sin emparejar
        jugador1 = lista_copia.pop(random.randint(0, len(lista_copia) - 1))
        jugador2 = lista_copia.pop(random.randint(0, len(lista_copia) - 1))
        emparejamientos.append((jugador1, jugador2))

    for pareja in emparejamientos:
        print(pareja[0]," VS ", pareja[1])

tenistas_top_8 = [
    "Jannik Sinner",
    "Alexander Zverev",
    "Carlos Alcaraz",
    "Taylor Fritz",
    "Casper Ruud",
    "Daniil Medvedev",
    "Novak Djokovic",
    "Álex de Miñaur"
]

tenistas_top_16 = [
    "Jannik Sinner", "Alexander Zverev", "Carlos Alcaraz", "Taylor Fritz",
    "Casper Ruud", "Daniil Medvedev", "Novak Djokovic", "Álex de Miñaur",
    "Stefanos Tsitsipas", "Andrey Rublev", "Grigor Dimitrov", "Hubert Hurkacz",
    "Holger Rune", "Ben Shelton", "Tommy Paul", "Karen Khachanov"
]

print("ENFRENTAMIENTOS")
emparejamiento_aleatorio(tenistas_top_8)
