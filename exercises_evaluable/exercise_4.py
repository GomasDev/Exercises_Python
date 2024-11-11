#Ejercicio 4 (1 punto). Crea una función que reciba como parámetros un número
# y dos unidades de medida: gramos, kilos o toneladas. La función devolverá la  cantidad recibida de
# la primera unidad de medida a la segunda unidad de medida. Utiliza la función para comprobar que funciona.
# Nota 1 tonelada = 1000 kilos y 1 kilo = 1000 gramos

def cambio(num,unid1,unid2):
    if unid1=="gramos":
        if unid2=="kilos":
            num=num*0.001
            return num
        else:
            #unid2=toneladas
            num=num*0.000001
            return num
    elif unid1=="kilos":
        if unid2=="gramos":
            num=num*1000
            return num
        else:
            num=num*0.001
            return num
    elif unid1=="toneladas":
        if unid2=="kilos":
            num=num*1000
            return num
        else:
            num=num*1000000
            return num

num=float(input("Introduce un numero: "))
unid1=input("Introduce su unidad de medida (kilos,gramos,toneladas): ")
unid1=unid1.lower()
unid2=input("Introduce a cual quieres pasarla (kilos,gramos,toneladas): ")
unid2=unid2.lower()

num=cambio(num,unid1,unid2)
print("La unidad es",num, unid2)