"""Ejercicio 8. TRAPPIST-1 es un sistema planetario ubicado a 40 años luz de la Tierra, en la constelación de Acuario. Su estrella es una enana roja ultrafría, mucho más pequeña y tenue que el Sol. En 2017, los astrónomos anunciaron el descubrimiento de siete planetas rocosos en este sistema, lo que lo convirtió en uno de los hallazgos más emocionantes de la astronomía moderna.
La siguiente lista muestra los datos que tenemos de los planetas del sistema TRAPPIST-1:
A partir de dicha lista y de la lista de los planetas del Sistema Solar hallar:
La masa media de los planetas del Sistema Solar vs la masa media de lo planetas de TRAPPIST-1
El planeta más denso de ambos sistemas
El planeta de TRAPPIST-1 cuya densidad más se parece a la de la Tierra
Los planetas sin lunas de ambos sistemas

"""

from Planeta import Planeta
from datetime import datetime
import statistics

planetas_trappist = [
    Planeta("TRAPPIST-1b", 0.85 * 5.972e24, 1.116 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1c", 1.38 * 5.972e24, 1.097 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1d", 0.388 * 5.972e24, 0.788 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1e", 0.692 * 5.972e24, 0.920 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1f", 1.04 * 5.972e24, 1.045 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1g", 1.32 * 5.972e24, 1.127 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1h", 0.326 * 5.972e24, 0.755 * 6.371e6, datetime(2017, 2, 22), [])
]

planetas = [
    Planeta("Mercurio", 3.301e23, 2.4397e6, datetime.min, []),
    Planeta("Venus", 4.867e24, 6.0518e6, datetime.min, []),
    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna", 1.737e6, 7.342e22]]),
    Planeta("Marte", 6.417e23, 3.3895e6, datetime.min, [["Fobos", 1.1e4, 1.0659e16], ["Deimos", 6.2e3, 1.4762e15]]),
    Planeta("Júpiter", 1.898e27, 6.9911e7, datetime.min, [
        ["Ganimedes", 2.634e6, 1.4819e23],
        ["Calisto", 2.410e6, 1.0759e23],
        ["Ío", 1.821e6, 8.9319e22],
        ["Europa", 1.560e6, 4.7998e22]
    ]),
    Planeta("Saturno", 5.683e26, 5.8232e7, datetime.min, [
        ["Titán", 2.575e6, 1.3452e23],
        ["Rea", 1.527e6, 2.3166e21],
        ["Japeto", 1.470e6, 1.8056e21],
        ["Dione", 1.123e6, 1.0955e21]
    ]),
    Planeta("Urano", 8.681e25, 2.5362e7, datetime.min, [["Titania", 1.578e6, 3.527e21]]),
    Planeta("Neptuno", 1.024e26, 2.4622e7, datetime.min, [["Tritón", 1.353e6, 2.14e22]]),
    Planeta("Plutón", 1.303e22, 1.1883e6, datetime(1930,2,18), [["Caronte", 6.057e5, 1.586e21]])
]

##La masa media de los planetas del Sistema Solar vs la masa media de lo planetas de TRAPPIST-1
masas_sistema_solar = [planeta.masa for planeta in planetas]
masas_trappist = [planeta.masa for planeta in planetas_trappist]

media_masa_solar = statistics.mean(masas_sistema_solar)
media_masa_trappist = statistics.mean(masas_trappist)

print("La media de las masas del sistema solar es: ", media_masa_solar)
print("La media de las masas del trappist es: ", media_masa_trappist)

if media_masa_solar > media_masa_trappist:
    print("La media de masas del sistema solar es mayor que la media del trappist.")
else:
    print("La media de masas del sistema trappist es mayor que la media del solar.")

##El planeta más denso de ambos sistemas
densidades_sistema_solar = [planeta.get_densidad() for planeta in planetas]
mayor_densidad_solar = max(densidades_sistema_solar)

densidades_sistema_trappist = [planeta.get_densidad() for planeta in planetas_trappist]
mayor_densidad_trappist = max(densidades_sistema_trappist)

print("El planeta con mayor densidad del sistema solar es: ")
for i, planeta in enumerate(planetas):
    if planeta.get_densidad() == mayor_densidad_solar:
        planeta_mayor_solar = planeta
        print(planeta_mayor_solar.nombre)
        break

print("El planeta con mayor densidad del sistema trappist es: ")
for i, planeta in enumerate(planetas_trappist):
    if planeta.get_densidad() == mayor_densidad_trappist:
        planeta_mayor_trappist = planeta
        print(planeta_mayor_trappist.nombre)
        break

##El planeta de TRAPPIST-1 cuya densidad más se parece a la de la Tierra
densidad_tierra = None
for planeta in planetas:
    if planeta.nombre == "Tierra":
        densidad_tierra = planeta.get_densidad()
        break

diferencia = [densidad_tierra - planeta.get_densidad() for planeta in planetas_trappist]
densidad_parecida = abs(min(diferencia))

for i, planeta in enumerate(planetas_trappist):
    if abs(densidad_tierra - planeta.get_densidad()) == densidad_parecida:
        print("El planeta con densidad mas parecida a la de la Tierra es: ", planeta.nombre)
        break

##Los planetas sin lunas de ambos sistemas
planetas_sin_luna_solar = []
planetas_sin_luna_trappist = []

print("Los planetas del sistema solar sin lunas son: ")
for planeta in planetas:
    if len(planeta.lunas) == 0:
        planetas_sin_luna_solar.append(planeta.nombre)

print(planetas_sin_luna_solar)

print("Los planetas del sistema solar trappist sin lunas son: ")
for planeta in planetas_trappist:
    if len(planeta.lunas) == 0:
        planetas_sin_luna_trappist.append(planeta.nombre)

print(planetas_sin_luna_trappist)
