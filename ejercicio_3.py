#Crea un programa que te pregunte dónde naciste primero y después dónde vives.
# El programa debe comparar si vives o no en el mismo sitio que naciste y mostrar
# un mensaje según sea el caso.

nacimiento=input("Donde naciste: ")
vives=input("Donde vives: ")
if nacimiento==vives:
    print("Vives en el mismo sitio que naciste")
else:
    print("No vives donde naciste")