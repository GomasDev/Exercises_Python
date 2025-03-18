#Ejercicio 15. Dadas las siguientes listas
# (la segunda contiene la masa de los
#planetas), encuentra el nombre del planeta
# de mayor masa y el de aquellos
#planetas cuya masa es superior a
# la masa media del sistema solar.
from exercises_list.exercise_6 import mayor

# Lista con los nombres de los planetas del sistema solar
planetas_sistema_solar = [
    "Mercurio", "Venus", "Tierra", "Marte",
    "Júpiter", "Saturno", "Urano", "Neptuno"
]
# Lista con las masas de los planetas en kilogramos (valores aproximados)
masas_sistema_solar = [
    3.3011e23, # Mercurio
    4.8675e24, # Venus
    5.97237e24, # Tierra
    6.4171e23, # Marte
    1.8982e27, # Júpiter
    5.6834e26, # Saturno
    8.6810e25, # Urano
    1.02413e26 # Neptuno
]

masa_media=sum(masas_sistema_solar)/len(masas_sistema_solar)

#sacar masa mayor a la media
print("Planeta mayor es: ")
for i, planeta in enumerate(planetas_sistema_solar):
    if masas_sistema_solar[i] > masa_media:
        print(planeta)


#sin acabar