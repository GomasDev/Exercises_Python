#Crea un programa que pida al usuario dos números y una operación
#(suma, resta, multiplicación, división) y realice la operación solicitada.

num1=int(input("Introduce un numero: "))
num2=int(input("Introduce un segundo numero: "))

operacion=input("Introduce tipo de operacion: (+,-,*,/)")

if operacion=="+":
    print(num1,"+",num2,"=",num1+num2)
elif operacion=="-":
    print(num1,"-",num2,"=",num1-num2)
elif operacion=="*":
    print(num1,"*",num2,"=",num1*num2)
else:
    print(num1,"/",num2,"=",num1/num2)