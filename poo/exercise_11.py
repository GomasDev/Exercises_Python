"""Ejercicio 11. Dada la anterior lista y la  siguiente que contiene los mejores libros escrito por españoles:
Encontrar los mejores libros de la historia que además son españoles
Encontrar los mejores escritores españoles cuyos libros NO estén dentro de los mejores libros escritos por la humanidad
Encontrar los mejores libros (españoles o mundiales) que empiezan por D (no puede haber repeticiones)
¿Quién es el mejor escritor español? (Calcular el mejor escritor español como aquel que que más títulos tiene en la lista
de mejores libros españoles)
"""

from Libro import Libro

libros = [
    Libro("Crimen y castigo", ["Fiódor Dostoievski"], 671, ["Novela", "Filosofía", "Psicológica"], 10),
    Libro("Guerra y paz", ["León Tolstói"], 1225, ["Novela", "Histórica"], 10),
    Libro("Anna Karénina", ["León Tolstói"], 864, ["Novela", "Drama", "Romance"], 9),
    Libro("El maestro y Margarita", ["Mijaíl Bulgákov"], 384, ["Fantasía", "Satírica"], 9),
    Libro("Los hermanos Karamázov", ["Fiódor Dostoievski"], 1013, ["Novela", "Filosofía", "Drama"], 10),
    Libro("1984", ["George Orwell"], 328, ["Distopía", "Ciencia ficción"], 10),
    Libro("Cien años de soledad", ["Gabriel García Márquez"], 471, ["Realismo mágico", "Drama"], 10),
    Libro("Ulises", ["James Joyce"], 730, ["Experimental", "Filosofía"], 8),
    Libro("Moby-Dick", ["Herman Melville"], 635, ["Aventura", "Clásico"], 9),
    Libro("Don Quijote de la Mancha", ["Miguel de Cervantes"], 863, ["Aventura", "Clásico", "Satíra"], 10)
]

libros2 = [
    Libro("Don Quijote de la Mancha", ["Miguel de Cervantes"], 863, ["Aventura", "Clásico", "Sátira"], 10),
    Libro("La Regenta", ["Leopoldo Alas \"Clarín\""], 928, ["Novela", "Realismo", "Drama"], 9),
    Libro("Fortunata y Jacinta", ["Benito Pérez Galdós"], 1056, ["Novela", "Costumbrismo", "Drama"], 9),
    Libro("Campos de Castilla", ["Antonio Machado"], 208, ["Poesía", "Reflexión"], 9),
    Libro("Platero y yo", ["Juan Ramón Jiménez"], 138, ["Narrativa", "Poesía en prosa"], 8),
    Libro("Bodas de sangre", ["Federico García Lorca"], 128, ["Teatro", "Tragedia", "Poesía"], 9),
    Libro("La colmena", ["Camilo José Cela"], 304, ["Novela", "Costumbrismo"], 8),
    Libro("Nada", ["Carmen Laforet"], 288, ["Novela", "Existencialismo"], 9),
    Libro("El camino", ["Miguel Delibes"], 176, ["Novela", "Realismo"], 8),
    Libro("Los santos inocentes", ["Miguel Delibes"], 254, ["Novela", "Drama social"], 9)
]

#Encontrar los mejores libros de la historia que además son españoles
print("Los mejores libros de la historia que ademas son españoles: ")
mejores_espanoles = []
for libro in libros2:
    for mejore in libros:
        if libro.nombre == mejore.nombre and libro.nombre not in mejores_espanoles:
            mejores_espanoles.append(mejore.nombre) #he creado lista para almacenar los libros

print(mejores_espanoles)

#Encontrar los mejores escritores españoles cuyos libros NO estén dentro de los mejores libros escritos por la humanidad
print("Los mejores escritores españoles cuyos libros NO estén dentro de los mejores libros escritos por la humanidad:")
mejores_excluidos = []
for libro in libros2:
    es_mejor = False  # Suponemos que no está en la lista de los mejores libros
    for mejor_libro in libros:
        if libro.nombre == mejor_libro.nombre:
            es_mejor = True
            break

    if not es_mejor and libro.autores not in mejores_excluidos: #he cerado lista para almecenar los autores
        mejores_excluidos.append(libro.autores)

print(mejores_excluidos)

#Encontrar los mejores libros (españoles o mundiales) que empiezan por D (no puede haber repeticiones)
print("Los mejores libros que empiezan por D: ")
lista_libros_d = []
for libro in libros + libros2:
    if libro.nombre[0] == "D" and libro.nombre not in lista_libros_d:
        lista_libros_d.append(libro.nombre)
print(lista_libros_d)

#¿Quién es el mejor escritor español? (Calcular el mejor escritor español como aquel que que más títulos tiene en la lista
#de mejores libros españoles)
print("El mejor escritor español (con más títulos en la lista de libros españoles):")

autores = []
cantidad_libros = []

for libro in libros2:
    for autor in libro.autores:
        if autor in autores:
            indice = autores.index(autor)
            cantidad_libros[indice] += 1
        else:
            autores.append(autor)
            cantidad_libros.append(1)

# Encontrar el autor con más libros
max_titulos = 0
mejor_escritor = ""

for i in range(len(autores)):
    if cantidad_libros[i] > max_titulos:
        max_titulos = cantidad_libros[i]
        mejor_escritor = autores[i]

print(mejor_escritor, "con ", max_titulos, " libros.")
