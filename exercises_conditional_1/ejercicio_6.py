#Crear un programa que te pida tu provincia de nacimiento y que te diga si eres andaluz o no

provincia=["Granada","Jaen","Almeria","Huelva","Cadiz","Sevilla","Cordoba"]

p_nacimiento=input("Donde naciste: ")

if p_nacimiento in provincia:
    print("Eres andaluz")
else:
    print("No eres andaluz")