#al haber usado in range, el codigo principal queda muy simple y moduladizado,
# por lo que es imposible crear funciones

palabra_level1 = "Luna"
palabra_level2 = "Bosque"
palabra_level3 = "Montaña"
vidas = 10
level = 1


while level <= 3:
    if level == 1:
        palabra_juego = palabra_level1
    elif level == 2:
        palabra_juego = palabra_level2
    else:
        palabra_juego = palabra_level3

    palabra_acertada = ["_" for _ in range(len(palabra_juego))]

    letras_ingresadas = []

    while vidas > 0 and "_" in palabra_acertada:

        print("---------")
        print("Nivel ", level)
        print("---------")

        print("Tienes ", vidas, " vidas.")
        print("Palabra que debes encontrar: ")
        print(palabra_acertada)  # si pongo *palabra_acertada se imprime la palabra sin comillas y sin []
        letra_usuario = input("Ingresa una letra: ")
        print("Has escrito esta letra: ", letra_usuario)




        encontrado = False

        for i, letra in enumerate(palabra_juego):
            if letra.lower() == letra_usuario.lower():
                palabra_acertada[i] = letra_usuario
                encontrado = True

        if encontrado:
            if letra_usuario in letras_ingresadas:
                print("Ya ingresaste esta letra: ", letra_usuario)
                print("Ingrese otra")
                continue
            else:
                letras_ingresadas.append(letra_usuario)
            print("Has encontrado una letra!!!! ✅ Te sumo una vida.")
            vidas += 1
            print("El numero de vidas es: ", vidas, "❤️")
        else:
            print("No existe la letra ❌")
            vidas -= 1
            print("Tienes -1 vida 💔. El numero de vidas es: ", vidas, "❤️")

    print(palabra_acertada) #si pongo *palabra_acertada se imprime la palabra sin comillas y sin []
    if "_" not in palabra_acertada:
        print("Has acertado la palabra completa 🏆🏆🏆🏆🏆")
        level += 1
    else:
        print("No te quedan vidas: ",vidas,"💔")
        print("Has perdido ☠️☠️")
        print("La palabra era: ", palabra_juego)
        break

if level > 3:
    print("¡Felicidades, has ganado el juego! 🎉")

