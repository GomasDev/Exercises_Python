#Crear un programa que te preguntes de dónde eres.
#  Si eres de Motril o de Granada te saludará,
#  si eres de cualquier otro sitio se despedirá de ti.

localidad=input("Dime de donde eres: ")
if localidad=="Motril" or localidad=="Granada":
    print("Hola buenos dias")
else:
    print("Hasta luego")