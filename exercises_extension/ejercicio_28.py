# Crea una función que imprima un mosaico rombo de anchura              ¡!¡!¡!¡!¡!!¡!¡!
#variable. (int: anchura) => void. Ejemplo ej28(9) imprimiría:

def rombo(n):
    for i in range(1,n+1):
        print(str(i)*i)
    for j in range(n,0,-1):
        print(str(j)*j)

anchura=int(input("Tamaño de ancho: "))
rombo(anchura)