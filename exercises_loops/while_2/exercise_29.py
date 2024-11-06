#Haz un programa que simule el registro de un usuario. Deberá
#pedirle su nombre y contraseña. Para asegurarnos que no escribe mal la
#contraseña se le pedirá que la ingrese dos veces. Mientras que las dos
#contraseñas no coincidan se le debe pedir que ingrese la contraseña.

nombre=input("Introduce el nombre: ")
contraseña=input("Introduce la contraseña: ")
contraseña2=input("Repite la contraseña: ")
while contraseña!=contraseña2:
    if contraseña!=contraseña2:
        print("ERROR, no coinciden")
        contraseña=input("Introduce la contraseña: ")
        contraseña2=input("Repite la contraseña: ")
print("Usuario creado")