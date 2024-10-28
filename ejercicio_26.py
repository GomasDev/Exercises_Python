#Crea un programa que pida un número al usuario
#  y haga una cuenta regresiva desde ese número
#  hasta 0, mostrando cada número en la pantalla.
#  Al llegar a 0, debe mostrar "Ring! Ring!"

num=int(input("Introduce un numero: "))
while num!=0:
    print(num)
    num-=1
print("RING!RING!")