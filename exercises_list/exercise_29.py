"""Ejercicio 29. Crea un programa que tenga una lista con los equipos de la liga
de fútbol ordenados según su posición en la liga. Haz que el programa lea el
nombre de equipos por teclado, si el equipo existe devolverá su posición en
la clasificación si no existe se informará que dicho equipo no existe pero el
programa NO debe fallar."""

liga = [
    "Real Madrid CF",
    "FC Barcelona",
    "Atlético de Madrid",
    "Sevilla FC",
    "Real Sociedad",
    "Real Betis",
    "Villarreal CF",
    "Athletic Bilbao",
    "Valencia CF",
    "Rayo Vallecano",
    "Granada CF",
    "Getafe CF",
    "Real Valladolid",
    "Elche CF",
    "Celta de Vigo",
    "RCD Espanyol",
    "CA Osasuna",
    "Levante UD",
    "Cádiz CF",
    "Deportivo Alavés"
]

equipo = input("Introduce un nombre de un equipo: ")

if equipo in liga:
    print("La posicion del equipo es: ",liga.index(equipo)+1)
else:
    print("El equipo no existe")