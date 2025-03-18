"""Ejercicio 10. A partir de la anterior lista:
Encontrar los libros escritos por Dostoievski con más de 1000 páginas
Encontrar los libros con menos de 400 páginas
Encontrar los libros cuyo nombre es un número
Encontrar (sin repetir) los escritores de la lista
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

#Encontrar los libros escritos por Dostoievski con más de 1000 páginas
print("Los libros escritos por Dostoievski y de mas de 1000 pag son: ")
for libro in libros:
    if libro.paginas > 1000:
        for autor in libro.autores:
            if "Fiódor Dostoievski" in autor:
                print(libro.nombre)

#Encontrar los libros con menos de 400 páginas
print("Los libros con menos de 400 pag son: ")
for libro in libros:
    if libro.paginas < 400:
        print(libro.nombre)

#Encontrar los libros cuyo nombre es un número
print("Los libros cuyo nombre es un numero: ")
for libro in libros:
    if libro.nombre.replace(" ","").isdigit(): #para que me cuente si hubiera espacio, 1 9 8 4.
        print(libro.nombre)

#Encontrar (sin repetir) los escritores de la lista
escritores = []
for libro in libros:
    for autor in libro.autores:
        if autor not in escritores:
            escritores.append(autor)
print(escritores)
