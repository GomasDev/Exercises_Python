import function

#inicializacion de variables
resultado=resultadoOperacion=aciertos=fallos=nPartida=nummin=nOperacion=nAcertadas=nFalladas=rachas=rachasmax=0
nVidas=vidaNuevo=3
nummax=10
logro_bronce=logro_plata=logro_oro=logro_platino=logro_master=logro_loser=salir=False
rachasplatino=0
while True:
    seleccion = function.imprimirMenu()
    nVidas=vidaNuevo
    aciertos=fallos=0
    match seleccion:
        case 0:
                print("Saliendo")
                break
        case 1:
            nPartida += 1
            rachas=rachasmax=0
            while nVidas>0:

                try:
                    resultadoOperacion=function.generarCuenta(nummin,nummax)
                    resultado =int(input("Introduce el resultado: "))

                except ValueError as error:
                    print(f"ERROR:{error}")
                    continue
                except Exception as error:
                    print(f"ERROR:{error}")
                    continue

                else:
                    if resultado==resultadoOperacion:
                        print("Correcto")
                        aciertos+=1
                        nAcertadas+=1
                        rachas+=1
                        if rachas>rachasmax:
                            rachasmax=rachas
                            if rachasmax==3 and logro_bronce==False:
                                logro_bronce=True
                                print("LOGRO DE BRONCE DESBLOQUEADO")
                                #function.mostrar_imagen('bronce_lol.jpeg',3)
                            if rachasmax==7 and logro_plata==False:
                                logro_plata=True
                                print("LOGRO DE PLATA DESBLOQUEADO")
                                #function.mostrar_imagen('plata_lol.jpeg', 3)
                            if rachasmax==10 and logro_oro==False:
                                logro_oro=True
                                print("LOGRO DE ORO DESBLOQUEADO")
                                # function.mostrar_imagen('oro_lol.jpeg', 3)
                            if rachasmax==10 and nummin>=10 and nummax>=15 and logro_platino==False:
                                logro_platino = True
                                print("LOGRO DE PLATINO DESBLOQUEADO")
                                #function.mostrar_imagen('platino_lol.jpeg', 3)
                            if rachasmax==20 and nummin>= 15 and nummax >= 50 and nVidas==1 and logro_master==False:
                                logro_master=True
                                print("LOGRO DE MASTER DESBLOQUEADO")
                                #function.mostrar_video('siu.mp4')
                    else:
                        nVidas-=1
                        fallos+=1
                        print("Incorrecto, el resultado era: ",resultadoOperacion)
                        print("Te quedan ",nVidas," vidas")
                        nFalladas+=1
                        rachas=0
                        if nVidas==0 and aciertos==0 and logro_loser==False:
                            logro_loser = True
                            print("LOGRO DE LOSER DESBLOQUEADO")
                    nOperacion+=1
                print("En tu partida numero ",nPartida," has acertado ",aciertos," y has fallado ",fallos)
                print("Has acertado un ",round(aciertos*100/(aciertos+fallos),2)," % de las cuentas")

        case 2:
            salir=False
            while not salir:
                print("La configuracion actual es: ")
                print("Numero de vidas: ",nVidas)
                print("Numero minimo: ",nummin)
                print("Numero maximo: ",nummax)
                selecionConfi=function.menuConfiguracion()
                match selecionConfi:
                    case 0:
                        print("Saliendo")
                        salir=True
                    case 1:
                        try:
                            vidaNuevo=int(input("Introduce el nuevo numero de vidas: (entre 1 y 10): "))

                        except ValueError as error:
                            print(f"ERROR:{error}")

                        except Exception as error:
                            print(f"ERROR:{error}")


                        else:
                            while vidaNuevo not in range(1,11):
                                try:
                                    vidaNuevo=int(input("Numero no valido, ha de ser entre 1 y 10: "))#Esta excepcion es cuando te equivocas, ya que hay un input diferente
                                except ValueError as error:
                                    print(f"ERROR:{error}")

                                except Exception as error:
                                    print(f"ERROR:{error}")

                                else:
                                    nVidas = vidaNuevo

                            nVidas = vidaNuevo
                    case 2:
                        try:
                            nuevomin = int(input("Introduce el numero de minimo: "))

                        except ValueError as error:
                            print(f"ERROR:{error}")

                        except Exception as error:
                            print(f"ERROR:{error}")


                        else:

                            while nuevomin>=nummax:
                                try:
                                    nuevomin = int(input("El numero minimo ha de ser menor al numero maximo: "))
                                except ValueError as error:
                                    print(f"ERROR:{error}")

                                except Exception as error:
                                    print(f"ERROR:{error}")

                                else:
                                    nummin = nuevomin

                            nummin=nuevomin
                    case 3:
                        try:
                            nuevomax = int(input("Introduce el numero de maximo: "))
                        except ValueError as error:
                            print(f"ERROR:{error}")

                        except Exception as error:
                            print(f"ERROR:{error}")

                        else:
                            while nuevomax <= nummin:
                                try:
                                    nuevomax = int(input("El numero maximo ha de ser mayor al numero minimo: "))
                                except ValueError as error:
                                    print(f"ERROR:{error}")

                                except Exception as error:
                                    print(f"ERROR:{error}")


                                else:
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
            if logro_loser:
                print("Logro de LOSER: OBTENIDO :(")
            else:
                print("Logro de LOSER: No acertas ninguna operacion :(")
