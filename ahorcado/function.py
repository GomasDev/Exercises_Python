def menuPrincipal() -> int:

    opcion = -1 #inciiar el valor fuera del rango
    while opcion not in range(0, 4):
        print("====JUEGO AHORCADO====")
        print("1.Jugar  🎮: ")
        print("2.Configuracion ⚙️: ")
        print("3.Estadisticas 📊:")
        print("0.Salir 🏃🏻‍♂️:")
        try:
            opcion = int(input("Que quieres hacer?: "))
            if opcion not in range(0, 4):  # Si no está en el rango, muestra un mensaje de error
                print("⚠️ Opción no válida. Ingrese un número entre 0 y 3.")
        except ValueError:
            print("⚠️ Opción no válida. Ingrese un número entre 0 y 3.")
        else:
            return opcion


def menuConfiguracion():
    opcion = -1  # inciiar el valor fuera del rango
    while opcion not in range(0, 3):
        print("===Configuracion AHORCADO===")
        print("1.Cambiar numero de vidas ❤️:")
        print("2.Cambiar palabra secreta 🔏: ")
        print("0.Salir 🏃🏻‍♂️:")
        try:
            opcion = int(input("Que quieres hacer?: "))
            if opcion not in range(0, 3):  # Si no está en el rango, muestra un mensaje de error
                print("⚠️ Opción no válida. Ingrese un número entre 0 y 3.")
        except ValueError:
            print("⚠️ Opción no válida. Ingrese un número entre 0 y 3.")
        else:
            return opcion