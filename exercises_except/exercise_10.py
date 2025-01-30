#Ejercicio 10. Crea un programa que te pida dos números y que te
# muestre por pantalla todos los números que hay entre el
# menor de los números introducidos y el mayor.


while True:
    try:
        num1=int(input("Introduce el primer numero: "))
        num2=int(input("Introduce el segundo numero: "))
    except ValueError as error:
        print(f"ERROR: {error}")

    else:
        if num1>num2:
            for i in range(num2+1,num1):    #el numero menor le sumamos 1 para que no lo cuente
                print(i)
        else:
            for i in range(num1+1,num2):
                print(i)

        seguir=input("Quieres seguir? (s/n): ").strip().lower()
        if seguir!="s":
            break