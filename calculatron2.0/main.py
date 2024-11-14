import function

#inicializacion de variables
resultado=0
nVidas=3
vidaNuevo=3
resultadoOperacion=0
aciertos=0
fallos=0
nPartida=0
nummin=0
nummax=10
nOperacion=0
nAcertadas=0
nFalladas=0
rachas=0
rachasmax=0
logro_bronce=False
logro_plata=False
logro_oro=False
logro_platino=False
logro_master=False

while True:
    seleccion = function.imprimirMenu()
    nVidas=vidaNuevo
    aciertos=0
    fallos=0
    match seleccion:
        case 0:
                print("Saliendo")
                break
        case 1:
            nPartida += 1
            rachas=0
            racha_platino=0
            racha_master=0
            while nVidas>0:
                resultadoOperacion=function.generarCuenta(nummin,nummax)
                resultado =int(input("Introduce el resultado: "))
                if resultado==resultadoOperacion:
                    print("Correcto")
                    aciertos+=1
                    nAcertadas+=1
                    rachas+=1
                    if rachas>rachasmax:
                        rachasmax=rachas
                        if rachasmax==3:
                            logro_bronce=True
                            print("LOGRO DE BRONCE DESBLOQUEADO")
                            function.mostrar_imagen('bronce_lol.jpeg',3)
                        elif rachasmax==7:
                            logro_plata=True
                            print("LOGRO DE PLATA DESBLOQUEADO")
                            function.mostrar_imagen('plata_lol.jpeg', 3)
                        elif rachasmax==10:
                            logro_oro=True
                            print("LOGRO DE ORO DESBLOQUEADO")
                            function.mostrar_imagen('oro_lol.jpeg', 3)

                            if rachasmax==10 and nummin >= 10 and nummax >= 15:
                                logro_platino=True
                                print("LOGRO DE PLATINO DESBLOQUEADO")
                                function.mostrar_imagen('platino_lol.jpeg', 3)
                        elif rachasmax==20 and nummin>= 15 and nummax >= 50 and nVidas==1:
                            logro_master=True
                            print("LOGRO DE MASTER DESBLOQUEADO")
                            function.mostrar_video('siu.mp4')


                else:
                    nVidas = nVidas - 1
                    fallos+=1
                    print("Incorrecto, el resultado era: ",resultadoOperacion)
                    print("Te quedan ",nVidas," vidas")
                    nFalladas+=1
                    rachas=0
                nOperacion+=1

            print("En tu partida numero ",nPartida," has acertado ",aciertos," y has fallado ",fallos)
            print("Has acertado un ",round(aciertos*100/(aciertos+fallos),2)," % de las cuentas")

        case 2:
            print("La configuracion actual es: ")
            print("Numero de vidas: ",nVidas)
            print("Numero minimo: ",nummin)
            print("Numero maximo: ",nummax)
            selecionConfi=function.menuConfiguracion()
            match selecionConfi:
                case 0:
                    print("Saliendo")
                case 1:
                    vidaNuevo=int(input("Introduce el nuevo numero de vidas: (entre 1 y 10: "))
                    while vidaNuevo<0 or vidaNuevo>10:
                        vidaNuevo=int(input("Numero no valido, ha de ser entre 1 y 10: "))
                        nVidas = vidaNuevo
                    nVidas = vidaNuevo
                case 2:
                    nuevomin=int(input("Introduce el numero de minimo: "))
                    if nummin>nummax:
                        nuevomin=int(input("El numero minimo ha de ser menor al numero maximo: "))
                        nummin=nuevomin
                    nummin=nuevomin
                case 3:
                    nuevomax = int(input("Introduce el numero de maximo: "))
                    if nummax < nummin:
                        nuevomax = int(input("El numero maximo ha de ser mayor al numero minimo: "))
                        nummax = nuevomax
                    nummax = nuevomax



        case 3:
            print("Has jugado un total de: ",nPartida)
            print("Habiendo realizado un total de ",nOperacion," operaciones")
            print("Has acertado un total de ",nAcertadas," operaciones")
            if nOperacion==0:
                print("Tu porcentaje de acierto es del 0%")
            else:
                print("Tu porcentaje de acierto es del ",int(nAcertadas*100/nOperacion),"%")
            print("Has fallado un total de ", nFalladas, " operaciones")
            if nOperacion==0:
                print("Tu porcentaje de fallos es del 0%")
            else:
                print("Tu porcentaje de fallos es del ",int(nFalladas*100/nOperacion),"%")
            print("Tu maxima racha de aciertos consecutivos es: ",rachasmax," aciertos")
        case 4:
            if logro_bronce:
                print("Logro de BRONCE: OBTENIDO :)")
            else:
                print("Logro de BRONCE: acierta tres operaciones consecutivas en una mismo partida->NO conseguido :(")
            if logro_plata:
                print("Logro de PLATA: OBTENIDO :)")
            else:
                print("Logro de PLATA: acierta siete operaciones consecutivas en una mismo partida->NO conseguido :(")
            if logro_oro:
                print("Logro de ORO: OBTENIDO :)")
            else:
                print("Logro de ORO: acierta diez operaciones consecutivas en una mismo partida->NO conseguido :(")
            if logro_platino:
                print("Logro de PLATINO: OBTENIDO :)")
            else:
                print("Logro de PLATINO: acierta diez operaciones consecutivas numero min>10 y numero maximo>15 en una mismo partida->NO conseguido :(")
            if logro_master:
                print("Logro de MASTER: OBTENIDO :)")
            else:
                print("Logro de MASTER: acierta 20 operaciones consecutivas numero min>10 y numero maximo>50 en una misma partida->NO conseguido :(")