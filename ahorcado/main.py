import function

palabra_juego = "Pepe"
vidas = vida_nueva = 3
num_palabra_acertadas = num_palabras_falladas = 0
nueva_palabra = palabra_juego

while True:
    vidas = vida_nueva
    palabra_juego = nueva_palabra
    palabra_acertada = ["_" for _ in range(len(palabra_juego))]
    #list comprehension
    # for _ in range(len(palabra_juego)):  Igual que lo de arriba
    #    palabra_acertada.append("_")
    # palabra_acertada = ["_"[] * len(palabra_juego)

    match function.menuPrincipal():
        case 1:

            while vidas > 0 and "_" in palabra_acertada:
                letra_usuario = input("Ingresa una letra: ")
                print("Has escrito esta letra: ", letra_usuario)
                encontrado = False
                for i, letra in enumerate(palabra_juego):
                    if letra.lower() == letra_usuario.lower():
                        palabra_acertada[i] = letra
                        encontrado = True
                if encontrado:
                    print("Existe la letra ✅")
                    print("El numero de vidas es: ", vidas, "❤️")
                else:
                    print("No existe la letra ❌")
                    vidas -= 1
                    print("El numero de vidas es: ", vidas, "❤️")

                print(*palabra_acertada) #Esto imprimirá cada elemento de la lista separado por un espacio
            if "_" not in palabra_acertada:
                print("Has acertado la palabra completa 🏆🏆🏆🏆🏆")
                num_palabra_acertadas += 1
            else:
                print("No te quedan vidas: ",vidas,"💔")
                num_palabras_falladas += 1
                print("La palabra era: ", palabra_juego)

        case 2:

            match function.menuConfiguracion():
                case 1:
                    vida_nueva = int(input("Ingresa una cantidad de vidas ❤️: "))
                case 2:
                    nueva_palabra = input("Ingresa una nueva palabra ❔:")
                case 0:
                    print("Saliendo al menu principal")

        case 3:

            print("El numero de palabras acertadas es 🟢: ", num_palabra_acertadas)
            print("El numero de palabras falladas es 🔴: ", num_palabras_falladas)

        case 0:
            break