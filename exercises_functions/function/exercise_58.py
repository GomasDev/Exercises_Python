#Crea una primera función que devuelva una operación aleatoria
#(suma, resta o multiplicación). Utilizando Crea una segunda función que
#dados dos números (inicial, final) muestre por pantalla cuentas (suma, resta
#o multiplicación) aleatorias donde los operandos estén entre los valores
#inicial y final, además la función deberá devolver el resultado de la operación
#generada. La segunda función debe de ayudarse de la primera función.
#Utiliza la segunda función para crear un programa que muestre por pantalla
#10 cuentas aleatorias, con inicio = 1 y final = 10. El usuario debe resolverlas y
#el programa indicarle si las acierta o no.
import random

def operador():
    operacion=random.randint(0,2)
    match operacion:
        case 0:
            operacion="+"
        case 1:
            operacion="-"
        case 2:
            operacion="*"
    return operacion

def calculador(inicio,final):
    num1=random.randint(inicio,final)
    num2=random.randint(inicio,final)
    operacion=operador()
    if operacion=="+":
        print(num1," + ",num2)
        resultado = num1 + num2
        return resultado
    elif operacion=="-":
        print(num1,"-",num2)
        resultado = num1 - num2
        return resultado
    elif operacion=="*":
        print(num1,"*",num2)
        resultado = num1 * num2
        return resultado

a=1
b=10
i=0
aciertos=0

while i!=10:
    resultado1=calculador(a,b)
    resultadoreal=int(input("Introduce el resultado: "))
    if resultadoreal==resultado1:
        print("Has acertado")
        aciertos=aciertos+1
        i = i + 1
    else:
        print("Has fallado")
        i = i + 1

print("Has llegado al ",b)
print("Has acertado ",aciertos)