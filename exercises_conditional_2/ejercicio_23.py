#Haz el ejercicio 13 pero utilizando la estructura match

#Además de if-elif… y match también podemos simular la estructura switch con mapas (estructura de datos), de hecho es la forma más eficiente de hacerlo (para el ordenador). En la UD5 aprenderás a utilizar los mapas (o diccionarios).

print("¿Qué quieres calcular?")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = input()

num1 = int(input("Introduce el primer número"))
num2 = int(input("Introduce el segundo número"))

match opcion:
    case "1":
        print(f"{num1} + {num2} = {num1+num2}")
    case "2":
        print(f"{num1} - {num2} = {num1-num2}")
    case "3":
        print(f"{num1} * {num2} = {num1*num2}")
    case "4":
        print(f"{num1} / {num2} = {num1/num2}")