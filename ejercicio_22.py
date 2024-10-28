#Crea un programa que calcule la tarifa de un
#  taxi según los kilómetros, la hora del día y
#  el día de la semana. Según las siguiente tarifas:
#Días de semana:
#Entre las 8 y las 18: 1€/km
#Entre las 19 y las 23: 1.2€/km
#Entre las 23 y las 7: 1.5€/km
#Sábados:
#Entre las 8 y las 18: 1.2€/km
#El resto del día: 1.5€/km
#Domingos:
#1.5€/km independientemente de la hora
#Además de los anterior tener en cuenta que nada
#  más coger el taxi se aplica una base de 3.5€.
#Nota: para simplificar los cálculos ten en cuenta
#  solo la hora de salida. Por lo tanto el usuario
# deberá especificar: día de la semana, hora que cogió
#  el taxi y kms que ha hecho

dia = input("Inserta el día de la semana: (L, M, X, J, V, S, D)")
hora = int(input("Inserta la hora en la que coges el taxi: "))
kms = float(input("Inserta el número de kms: "))

if dia == "S":
    if hora>=8 and hora <=18:
        tarifa = 1.2
    else:
        tarifa = 1.5
elif dia == "D":
    tarifa = 1.5
# El resto de días, es decir entre semana
else:
    if hora>=8 and hora<=18:
        tarifa = 1
    elif hora>=19 and hora<23:
        tarifa = 1.2
    elif hora == 23 or hora>=0 and hora<=7:
        tarifa = 1.5

coste = 3.5 + (tarifa * kms)
print(f"Supuesto que coges el taxi en {dia} a las {hora} horas y haces {kms} kilometros, el viaje te costaría {coste}")