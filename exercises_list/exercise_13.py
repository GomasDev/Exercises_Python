#Ejercicio 13. Utilizando las listas del ejercicio
# 12 encuentra el nombre de los
#meses en los que llueve más que la media

precipitaciones_granada_2023 = [
     40.2, # Enero
     35.6, # Febrero
     45.8, # Marzo
     50.1, # Abril
     30.3, # Mayo
     10.4, # Junio
     1.2, # Julio
     5.6, # Agosto
     20.8, # Septiembre
     60.5, # Octubre
     55.3, # Noviembre
     42.7 # Diciembre
]

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

preci_max=precipitaciones_granada_2023[0]
suma = sum(precipitaciones_granada_2023)
media = suma / len(precipitaciones_granada_2023)
for i, precipitacion in enumerate(precipitaciones_granada_2023):
    if precipitacion > media:
        print("los meses on las precipitacion que la media son: ", meses[i])

media = suma / len(precipitaciones_granada_2023)
print("La media es: ", round(media, 2))