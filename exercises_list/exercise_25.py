"""Ejercicio 25. Amplía el programa del ejercicio 20 para que se puedan
completar tareas y que al hacerlo desaparezcan de la lista. En concreto
cuando se muestren las tareas pendientes haz que si el usuario inserta un
número de tarea válido (0 para salir al menú principal) se complete dicha
tarea: """

lista_tareas = ["Comprar", "fruta", "Estudiar programación", "Desinstalar el LOL"]

while True:
    print("______________________________")
    print("1.Ver tareas pendientes")
    print("2.Agregar tareas pendientes")
    print("0.Salir")
    opcion = int(input("Bienvenido a la APP de tareas, elige opcion(1, 2 o 0: "))
    print("_____________________________________________________________")
    match opcion:
        case 1:
            print("Lista Tareas Pendientes")
            print("_______________________")
            while True:
                for i, tarea in enumerate(lista_tareas):
                    print(i+1, tarea)

                print(len(lista_tareas)+1, ".Salir")
                opcion = int(input("Has completado alguna tarea?: "))

                if opcion >0:
                    if opcion == len(lista_tareas)+1:
                        break
                    else:
                        print("Has completado la siguiente tarea, enhorabuena")
                        lista_tareas.pop(opcion-1)
                else:
                    print("No hay tareas pendientes")

        case 2:
            print("Agregando Tareas")
            tareas = input("Introduce nueva Tarea: ")
            n = int(input("Introduce la prioridad: "))
            lista_tareas.insert(n-1,tareas)
        case 0:
            print("Saliendo")
            break
