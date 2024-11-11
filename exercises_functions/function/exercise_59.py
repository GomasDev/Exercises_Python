#Crea el fichero aleatorio.py que contenga las siguientes
#funciones:
#● lanzarMoneda()→ simula el lanzamiento de una moneda imprime por
#pantalla, de forma aleatoria, cara o cruz
#● lanzarMonedas(n: int)→ simula el lanzamiento de n monedas
#utilizando la función lanzarMoneda()
#● lanzarDado()
#● lanzarDados(n: int)
#Crea un el fichero ejercicio59.py dónde importes aleatorio.py. Haz uso de
#cada una de las funciones para comprobar que funciona correctamente.
import random


def lanzarMoneda():
    lado=random.randint(0,1)
    if lado==0:
        resultado="Cruz"
        return resultado
    elif lado==1:
        resultado="Cara"
        return resultado

def lanzarMonedas(n):
    for i in range(n):
        resultado=lanzarMoneda()
        print(resultado)

lanzarMonedas(10)