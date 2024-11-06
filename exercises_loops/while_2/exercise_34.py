#Crea un programa que defina un número secreto. El usuario
#deberá descubrirlo. Cuando falle se le informará de si el número secreto es
#mayor o menor al introducido. Cuando acierte el número se le informará del
#número de intentos que ha necesitado para calcularlo.

numsecreto=45
encontrado=False
intento=0
while encontrado==False:
    num=int(input("Introduce un numero: "))
    intento=intento+1
    if num<numsecreto:
        print("El numero es menor que el numero secreto")
        
    elif num==numsecreto:
        print("Has encontrado el numero secreto")
        print("El numero de intentos es: ",intento)
        encontrado=True
    else:
        print("El numero es mayor que el numero secreto")