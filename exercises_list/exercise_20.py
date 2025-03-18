#Ejercicio 20. Crea un programa para gestionar una lista de tareas
#pendientes. La lista comenzará con las siguientes tareas: ["Comprar
#fruta", "Estudiar programación", "Desinstalar el LOL"]. El
#programa permitirá ver la lista de tareas pendientes e insertar nuevas tareas
#en la posición que se desee. <
#Al iniciarse el programa:
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
            for i, tarea in enumerate(lista_tareas):
                print(i+1, tarea)
        case 2:
            print("Agregando Tareas")
            tareas = input("Introduce nueva Tarea: ")
            n = int(input("Introduce la prioridad: "))
            lista_tareas.insert(n-1,tareas)
        case 0:
            print("Saliendo")
            break
