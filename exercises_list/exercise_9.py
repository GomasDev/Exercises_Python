#Ejercicio 9. Crea una lista con el nombre de todos los países de Europa.
#Muestra por pantalla el nombre de aquellos países que tengan 6 o menos
#letras.

paises_europa = [
    "Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyán",
    "Bélgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria",
    "Chipre", "Ciudad del Vaticano", "Croacia", "Dinamarca", "Eslovaquia",
    "Eslovenia", "España", "Estonia", "Finlandia", "Francia", "Georgia",
    "Grecia", "Hungría", "Irlanda", "Islandia", "Italia", "Kazajistán",
    "Kosovo", "Letonia", "Liechtenstein", "Lituania", "Luxemburgo",
    "Macedonia del Norte", "Malta", "Moldavia", "Mónaco", "Montenegro",
    "Noruega", "Países Bajos", "Polonia", "Portugal", "Reino Unido",
    "República Checa", "Rumanía", "Rusia", "San Marino", "Serbia",
    "Suecia", "Suiza", "Turquía", "Ucrania"
]


for pais in paises_europa:
    if len(pais.replace(" ","")) <=6: #quitar espacios
        print(pais)