#Ejercicio 11. Dada la siguiente lista:
#Encuentra la posición en la lista del Real Betis


liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona",
    "Athletic Club", "Villarreal CF", "RCD Mallorca", "Rayo Vallecano"
    , "Girona FC", "Real Sociedad", "Real Betis", "CA Osasuna",
    "Sevilla FC", "RC Celta", "Getafe CF", "UD Las Palmas",
    "CD Leganés", "Deportivo Alavés", "RCD Espanyol",
    "Valencia CF", "Real Valladolid"]

for i, equipo in enumerate(liga):
    if equipo == "Real Betis":
        print("La posicion es: ", i+1)