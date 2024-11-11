import random
import time
import os
from PIL import Image


#seleccion de operandos
def operador():
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
def generarCuenta(numMin,numMax):
    num1=random.randint(numMin,numMax)
    num2=random.randint(numMin,numMax)
    operacion=operador()
    if operacion=="%" and operacion=="/":
        while num2==0:
            num2=random.randint(numMin,numMax)

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
        print(num1,"/",num2,"= ?" )
        resultado = num1 // num2
        print(resultado)
        return resultado
    elif operacion=="%":
        print(num1,"%",num2,"= ?" )
        resultado = num1 % num2
        print(resultado)
        return resultado


#Menu Principal
def imprimirMenu():
    print("====BIENVENIDO AL CALCULATRON 2.0====!!!!!")
    print("1.Jugar")
    print("2.Configuracion")
    print("3.Estadisticas")
    print("4.Logro")
    print("0.Salir")
    seleccion=int(input("Selecciona una opcion: "))
    return seleccion
#Menu configuracion
def menuConfiguracion():
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
    time.sleep(tiempo)
    if os.name=="posix":
        os.system("pkill -f display")
    elif os.name=="nt":
        os.system("taskkill /f /im dllhost.exe")