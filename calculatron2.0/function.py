import random
import time
import os
from PIL import Image
import cv2

#seleccion de operandos
def operador()->str:
    operacion=random.randint(0,4)
    match operacion:
        case 0:
            operacion="+"
        case 1:
            operacion="-"
        case 2:
            operacion="*"
        case 3:
            operacion="/"
        case 4:
            operacion="%"
    return operacion

#operaciones
def generarCuenta(numMin:int,numMax:int)->int:
    num1=random.randint(numMin,numMax)
    num2=random.randint(numMin,numMax)
    operacion=operador()
    if operacion=="+":
        print(num1," + ",num2,"= ?")
        resultado = num1 + num2
        print(resultado)
        return resultado
    elif operacion=="-":
        print(num1,"-",num2,"= ?")
        resultado = num1 - num2
        print(resultado)
        return resultado
    elif operacion=="*":
        print(num1,"*",num2,"= ?" )
        resultado = num1 * num2
        print(resultado)
        return resultado
    elif operacion=="/":
        if num2==0:
            while num2==0:
                num2 = random.randint(numMin, numMax)
        print(num1,"/",num2,"= ?" )
        resultado = num1 // num2
        print(resultado)
        return resultado
    elif operacion=="%":
        if num2==0:
            while num2==0:
                num2 = random.randint(numMin, numMax)
        print(num1,"%",num2,"= ?" )
        resultado = num1 % num2
        print(resultado)
        return resultado

#Menu Principal
def imprimirMenu()->int:
    print("====BIENVENIDO AL CALCULATRON 2.0====!!!!!")
    print("1.Jugar")
    print("2.Configuracion")
    print("3.Estadisticas")
    print("4.Logro")
    print("0.Salir")
    seleccion=int(input("Selecciona una opcion: "))
    return seleccion

#Menu configuracion
def menuConfiguracion()->int:
    print("1.Cambiar numero de vidas")
    print("2.Cambiar numero minimo")
    print("3.Cambiar numero maximo")
    print("0.Salir")
    seleccion=int(input("¿Que desea hacer? "))
    return seleccion

#generar imagen
def mostrar_imagen(ruta,tiempo):
    imagen=Image.open(ruta)
    imagen.show()
    #time.sleep(tiempo)

#generar video
def mostrar_video(ruta):
    # Abre el archivo de video
    cap = cv2.VideoCapture(ruta)

    # Verifica si el archivo de video se abrió correctamente
    if not cap.isOpened():
        print("Error al abrir el archivo de video")
        return

    # Reproduce el video hasta que termine o se presione la tecla 'q'
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
            # Espera 30 ms entre frames (ajustable) y sale si se presiona 'q'
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:
            break
    # Libera los recursos y cierra las ventanas
    cap.release()
    cv2.destroyAllWindows()