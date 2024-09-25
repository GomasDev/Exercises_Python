#Crea una función que dada la longitud de los tres lados de un triángulo
#determina el tipo de triangulo, i.e.: equilátero, isósceles o escaleno, que es. (int[]:
#longitudes) => (string: tipo)

def tipo_triangulo(lado1,lado2,lado3):
    if lado1==lado2==lado3:
        tipo="Equilatero"
        return tipo
    else:
        if lado1==lado2:
            tipo="Isosceles"
            return tipo
        else:
            tipo="Escaleno"
            return tipo


lado1=input("Introduce longitud de un lado: ")
lado2=input("Introduce longitud de segundo lado: ")
lado3=input("Inrtoduce longitud de lado 3: ")
print("El triangulo es ",tipo_triangulo(lado1,lado2,lado3))
