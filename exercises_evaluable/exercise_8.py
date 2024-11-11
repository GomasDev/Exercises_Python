"""Ejercicio 8 (2 puntos).  Crea una función que genere una carta al azar.
La carta estará compuesta por un palo (oros, copas, bastos y espadas) y
por un número (del 1 al 10) o una figura (sota, caballo y rey).
La función devolverá una cadena de texto que represente a la carta, ejemplo: “7 de copas”
Usando la función crea un programa que te pida una carta y que muestre cartas
al azar hasta que salga la carta que introdujiste informándote del número de carta en cada momento. Ejemplo:
"""
import random

def carta():
    eleccionPalo=random.randint(0,3)
    palo=None
    match eleccionPalo:
        case 0:
            palo="oros"
        case 1:
            palo="copas"
        case 2:
            palo="espadas"
        case 3:
            palo="bastos"
    eleccionNum=random.randint(0,12)
    num=None
    match eleccionNum:
        case 0:
            num="1"
        case 1:
            num="2"
        case 2:
            num="3"
        case 3:
            num="4"
        case 4:
            num="5"
        case 5:
            num="6"
        case 6:
            num="7"
        case 7:
            num="8"
        case 8:
            num="9"
        case 9:
            num="10"
        case 10:
            num="sota"
        case 11:
            num="caballo"
        case 12:
            num="rey"
    return palo,num
eleccionPalo=input("Elige el palo de la carta(oros, copas, bastos y espadas): ")
eleccionNum=input("Elige el numero o la figura de la carta (1 al 10 o sota, caballo y rey): ")
palo=None
num=None
n=1
eleccion=True
while eleccion==True:
    palo,num=carta()
    if eleccionNum==num and eleccionPalo==palo:
        print("Carta ", n, ": ", num, " de ", palo)
        eleccion = False
    else:
        print("Carta ",n,": ",num," de ",palo)
    n+=1
