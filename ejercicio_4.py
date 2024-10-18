#Crear un programa que te pregunte por tu edad y lugar de nacimiento.
# Si eres mayor de edad y de Motril te saludará en cualquier otro caso se despedirá de ti.

edad=int(input("Introduce tu edad: "))
nacimiento=input("Introduce lugar de nacimiento: ")

if edad>=18 and nacimiento=="Motril":
    print("Hola buenos dias")
else:
    print("Hasta luego")