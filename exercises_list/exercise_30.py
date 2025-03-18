"""Ejercicio 30. Crea un programa que contenga 3 listas: una con el nombre de
los 8 planetas del Sistema Solar, otra con sus respectivas masas y otra con
sus respectivos radios. Cuando insertes por teclado el nombre de un planeta
el programa deberá la siguiente información: su posición en el Sistema Solar,
su masa y su radio."""


# Lista con el nombre de los 8 planetas del Sistema Solar
sistema_solar = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

# Lista con las masas (en 10^24 kg) de cada planeta, en el mismo orden
masas = [0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102]

# Lista con los radios (en km) de cada planeta, en el mismo orden
radios = [2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622]


planeta = input("Ingrese el nombre del planeta: ")

if planeta in sistema_solar:
    print("La posicion en el sistema solar es: ",sistema_solar.index(planeta)+1)
    print("La masa del planeta es: ",masas[sistema_solar.index(planeta)])
    print("El radio del planeta es: ",radios[sistema_solar.index(planeta)])