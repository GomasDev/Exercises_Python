#Crea un programa que simule un captcha de resolver una
#pequeña operación matemática de una suma. Si el usuario falla se le deberá
#volver a preguntar hasta que acierte.

num1=3
num2=5

catcha=num1+num2
print(num1,"+",num2)
num=int(input("Introduce la respuesta del catcha: "))
while num!=catcha:
    print(num1,"+",num2)
    num=int(input("Introduce la respuesta del catcha: "))
print("Respuesta correcta")