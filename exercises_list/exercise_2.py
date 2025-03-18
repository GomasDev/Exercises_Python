#Ejercicio 2. Crea una lista con el nombre de los
# planetas del sistema solar.
#Muestra por pantalla aquello que empiecen por la letra M.

# Lista de los planetas del Sistema Solar
planetas = [
    "Mercurio",
    "Venus",
    "Tierra",
    "Marte",
    "Júpiter",
    "Saturno",
    "Urano",
    "Neptuno"
]

for i in planetas:
    if i[0].lower()=="m":
        print(i)