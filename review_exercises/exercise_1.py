"""Ejercicio 1. Un hotel de lujo de Mónaco alquila habitaciones.
 El precio de la habitación varía según si es individual o doble
 y según si tiene vistas al mar o no.

                    Individual      Doble

Con vistas al mar   4800€           8000€
Sin vistas al mar   1600€           2400€

Crea una función que según el tipo de habitación y el número de días
 que se alquile calcule el precio total. Tener en cuenta que si se
 alquila una habitación 7 días o más entonces el hotel aplica un
 increíble descuento del 2% a partir del séptimo día.

Una vez creada la función crea un programa que pida los datos
al usuario y calcule el precio a pagar."""

def alquiler(tipos:str,dia:int)->float:
    vistas=input("Quieres la habitacion con vistas?(si o no):")
    if vistas.lower()=="si":
        precio=4800 if tipos.lower()=="doble" else 8000
    else:
        precio=1600 if tipos.lower()=="individual" else 2400
    return precio*dia

tipo=input("Introduce el tipo de habitacion (individual o doble): ")
dias=int(input("Introduce los dias que quieres la habitacion: "))
precioTotal=alquiler(tipo,dias)
if dias>=7:
    precioTotal*=0.8
print("El precio total es: ",precioTotal)