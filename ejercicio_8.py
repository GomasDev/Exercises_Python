#El despliegue de páginas web es un contenido que se aprende
#en el primer curso de ASIR y en el segundo curso de DAW.
#Crea un programa que dado el ciclo y el curso determine
#si se aprende a desplegar páginas web.

ciclo=["SMR","ASIR","DAW","DAM"]

ciclo_alumno=input("Introduce el ciclo del alumno (SMR,ASIR,DAW,DAM): ")
if ciclo_alumno in ciclo:
    curso_alumno=int(input("Introduce el curso del alumno: "))
    if (ciclo_alumno=="DAW" and curso_alumno==2 )or (ciclo_alumno=="ASIR" and curso_alumno==1 ) :
        print("Tiene que cursar la asignatura de despliegue.")
    else:
        print("No tiene la asignatura de despliegue.")
else:
    print("No existe ese ciclo.")