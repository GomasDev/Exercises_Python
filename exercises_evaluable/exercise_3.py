#Ejercicio 3 (2 puntos). Crea un programa que calcule el precio de
# la habitación de un hostal según el día de la semana, el tipo de
# habitación (individual o doble) si el día es festivo o no y de si ç
# se dispone de un cupón de descuento.
#Tabla de precios
#Día de la semana        Tipo habitación         Precio
#De lunes a jueves          Individual               30€
#                            Doble                   50€
#Viernes y sábado            Individual              45€
#                            Doble                   70€
#Domingo                     Individual              40€
#                           Doble                   60€
#Si el día es festivo se aplicarán las tarifas de los viernes
# y sábados independientemente de qué día de la semana sea.
#Si el se dispone de cupón de descuento pedirá especificar la
# cuantía del descuento en porcentaje (un número entre 0 y 100) y se deberá aplicar el descuento.

dia=input("Introduce dia: ")
habitacion=input("Introduce habitacion: (individual o doble)")
festivo=input("Introduce si es festivo: (si o no)")
vCupon=input("Dispones de cupon de descuento?: (si o no)")
if vCupon.lower()=="si":
    cupon=float(input("Introduce cupon: (0-100)"))
    cupon=cupon*0.01

if dia.lower()=="lunes" or dia.lower()=="martes" or dia.lower()=="miercoles" or dia.lower()=="jueves":
    if habitacion.lower()=="individual":
        if festivo.lower()=="si":
            precio = 45
            if vCupon.lower()=="si":
                precio=precio*(1-cupon)
            print("El precio de la individual es: ", precio)
        else:
            precio = 30
            if vCupon.lower() == "si":
                precio = precio * (1 - cupon)
            print("El precio de la individual es: ", precio)
    else:
        if festivo.lower()=="si":
            precio = 70
            if vCupon.lower() == "si":
                precio = precio * (1 - cupon)
            print("El precio de la doble es: ", precio)
        else:
            precio=50
            if vCupon.lower() == "si":
                precio = precio * (1 - cupon)
            print("El precio de la doble es: ",precio)
elif dia.lower()=="viernes" or dia.lower()=="sabado":
    if habitacion.lower()=="individual":
        precio=45
        if vCupon.lower() == "si":
            precio = precio * (1 - cupon)
        print("El precio de la individual es: ",precio)
    else:
        precio=70
        if vCupon.lower() == "si":
            precio = precio * (1 - cupon)
        print("El precio de la doble es: ",precio)
elif dia.lower()=="domingo":
    if habitacion.lower()=="individual":
        precio=40
        if vCupon.lower() == "si":
            precio = precio * (1 - cupon)
        print("El precio de la individual es: ",precio)
    else:
        precio=60
        if vCupon.lower() == "si":
            precio = precio * (1 - cupon)
        print("El precio de la doble es: ",precio)