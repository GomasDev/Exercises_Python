#Crea un programa con dos variables. Una que contenga el
# ciclo en el que está matriculado un alumno (SMR, ASIR, DAW, DAM)
#  y otra que contenga el curso en el que ésta (1 o 2).
# El programa debe mostrar en pantalla si dicho alumno tiene
# que cursar la asignatura de programación (dicha asignatura
# la tienen los alumnos de primer curso de DAW o DAM)

ciclo=["SMR","ASIR","DAW","DAM"]

ciclo_alumno=input("Introduce el ciclo del alumno (SMR,ASIR,DAW,DAM): ")
if ciclo_alumno in ciclo:
    curso_alumno=int(input("Introduce el curso del alumno: "))
    if (ciclo_alumno=="DAW" or "DAM") and curso_alumno==1:
        print("Tiene que cursar la asignatura de programacion.")
    else:
        print("No tiene la asignatura de programacion.")
else:
    print("No existe ese ciclo.")