"""Ejercicio 1. Dadas las siguientes listas:
Crea un programa que muestre por pantalla:
La población media de dichos países.
El nombre del país menos poblado."""
import statistics

paises = ["Alemania", "Francia", "Italia", "España", "Paises Bajos", "Polonia", "Suecia", "Belgica", "Austria", "Portugal"]
poblaciones = [83, 68, 59, 47, 17, 38, 10, 11, 9, 10] # En millones de habitantes

media = statistics.mean(poblaciones)
print("La poblacion media de dichos paises es: ", media)

for i, poblacion in enumerate(poblaciones):
    if poblacion == min(poblaciones):
        print("El pais menos poblado es: ", paises[i],"con ", poblacion, " millones de habitantes.")