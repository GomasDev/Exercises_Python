"""Ejercicio 1. Crea un programa que muestre un menú que permita calcular:
● El perímetro de un triángulo
● El área de un triángulo
● El perímetro de un rectángulo
● El área de un rectángulo
● Si un rectángulo es un cuadrado"""


def num_valido(base:float, altura:float)->bool:
    if base <= 0 or altura <= 0:
        return False
    else:
        return True

def es_triangulo(lado1:float, lado2:float, lado3:float)->bool:
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        print("No es triangulo, tiene algun lado de tamaño 0")
        return False
    elif lado1+lado2<=lado3 or lado1+lado3<=lado2 or lado2+lado3<=lado1:
        print("No es triangulo, no tiene un lado mayor que el suma de los otros dos")
        return False
    else:
        return True

def perimetro_triangulo():
    print("Perimetro Triangulo")
    try:
        a = float(input("Ingrese el lado a: "))
        b = float(input("Ingrese el lado b: "))
        c = float(input("Ingrese el lado c: "))
    except ValueError as error:
        print(f"ERROR:{error}")
    else:
        if es_triangulo(a, b, c):
            print(f"El perimetro del triangulo es: {a + b + c}")

def area_triangulo():
    print("Area Triangulo")
    try:
        base_t = float(input("Ingrese la base: "))
        altura_t = float(input("Ingrese la altura: "))
    except ValueError as error:
        print(f"ERROR:{error}")
    else:
        if num_valido(base_t, altura_t):
            print(f"El area del triangulo es: {base_t * altura_t / 2}")
        else:
            print("No es triangulo")

def perimetro_rectangulo():
    try:
        print("Perimetro Rectangulo")
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
    except ValueError as error:
        print(f"ERROR:{error}")
    else:
        if num_valido(base, altura):
            print(f"El perimetro del rectangulo es: {base * 2 + altura * 2}")
        else:
            print("No es rectangulo")

def area_rectangulo():
    print("Area Rectangulo")
    try:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
    except ValueError as error:
        print(f"ERROR:{error}")
    else:
        if num_valido(base, altura):
            print(f"El area del rectangulo es: {base * altura}")
        else:
            print("No es rectangulo")

def cuadrado():
    print("Afirmacion Cuadrado")
    try:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
    except ValueError as error:
        print(f"ERROR:{error}")
    else:
        if num_valido(base, altura):
            if base == altura:
                print("Es cuadrado")
            else:
                print("No es cuadrado")
        else:
            print("No es cuadrado")

def menu():
    print("====MENU====")
    print("1. Perimetro Triangulo")
    print("2. Area Triangulo")
    print("3. Perimetro Rectangulo")
    print("4. Area Rectangulo")
    print("5. Afirmacion Cuadrado")
    print("6. Salir")

def main():
    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError as error:
            print(f"ERROR:{error}")
        else:
            if opcion not in range(1, 7):
                print("Opcion no valida")
                continue
            match opcion:
                case 1:
                    perimetro_triangulo()
                case 2:
                    area_triangulo()
                case 3:
                    perimetro_rectangulo()
                case 4:
                    area_rectangulo()
                case 5:
                    cuadrado()
                case 6:
                    print("Saliendo")
                    break


if __name__ == "__main__":
    main()