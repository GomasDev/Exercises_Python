#Ejercicio 22. Crea una lista con las asignaturas del primer curso DAW y otra
#con las del segundo curso. Usando .extend crea una tercera lista que
#contenga todas las asignaturas de DAW.

daw1 = ["Programacion", "SI", "BBDD"]
daw2 = ["IPE", "Dlespliegue", "pene"]
daw_completo2 = []

daw_completo = daw1 + daw2
daw_completo2.extend(daw1)
daw_completo2.extend(daw2)

print(daw_completo2)
print(daw_completo)