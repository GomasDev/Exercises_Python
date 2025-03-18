#Ejercicio 10. Crea una lista con los nombres de los jugadores de tu equipo de
#fútbol favorito. Muestra por pantalla el nombre de aquellos jugadores cuyo
#nombre empiece por la misma letra que acaba.

# Lista de jugadores del Atlético de Madrid para la temporada 2024-2025
jugadores_atletico_madrid = [
    # Porteros
    "Jan Oblak",
    "Juan Musso",
    "Antonio Gomisa",
    "Alejandro Iturbe",

    # Defensores
    "César Azpilicueta",
    "José María Giménez",
    "Javi Galán",
    "Ilias Kostis",
    "Robin Le Normand",
    "Nahuel Molina",
    "Reinildo Mandava",

    # Centrocampistas
    "Koke",
    "Pablo Barrios",
    "Rodrigo De Paul",
    "Conor Gallagher",
    "Saúl Ñíguez",

    # Delanteros
    "Antoine Griezmann",
    "Ángel Correa",
    "Álvaro Morata",
    "Samuel Lino",
    "Javi Serrano"
]


for jugador in jugadores_atletico_madrid:
    if jugador[0].lower() == jugador[len(jugador) - 1].lower():
        print(jugador)