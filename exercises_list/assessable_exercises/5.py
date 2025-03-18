"""Ejercicio 5. Dada una matriz como la siguiente (columna 2 son el número de
habitantes y la 4 el área):
Crea una función que recibido un continente y la lista de países devuelva el
país con mayor densidad de población (población/área).
"""

def pais_con_mayor_densidad(continente, paises):
    mayor_densidad = 0
    pais_densidad_maxima = ""

    for pais in paises:
        if pais[3] == continente:
            poblacion = pais[2]
            area = pais[4]
            densidad = poblacion / area  # calculamos densidad

            if densidad > mayor_densidad:
                mayor_densidad = densidad
                pais_densidad_maxima = pais[0]

    return pais_densidad_maxima

# ejemplos de uso
paises = [
    ["Argentina", "Buenos Aires", 46000000, "América", 2780400],
    ["España", "Madrid", 48000000, "Europa", 505990],
    ["Japón", "Tokio", 125000000, "Asia", 377975],
    ["Sudáfrica", "Pretoria", 60000000, "África", 1221037],
    ["Australia", "Canberra", 26000000, "Oceanía", 7692024],
    ["Canadá", "Ottawa", 38000000, "América", 9984670]
]

print(pais_con_mayor_densidad("América", paises))
