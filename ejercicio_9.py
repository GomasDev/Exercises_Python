#Crea un programa que determine si un alumno/a debe realizar
# las prácticas de empresa. Las prácticas de empresa son realizadas
#  por los alumnos de segundo curso de cualquier ciclo.

ciclo=["SMR","ASIR","DAW","DAM"]

ciclo_alumno=input("Introduce el ciclo del alumno (SMR,ASIR,DAW,DAM): ")
curso_alumno=int(input("Introduce el curso del alumno: "))
if ciclo_alumno in ciclo and curso_alumno==2:
    print("Tiene que hacer practicas")
else:
    print("No tiene que hacer practicas")