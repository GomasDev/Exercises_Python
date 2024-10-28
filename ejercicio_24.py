#Haz un programa que simule el registro de un usuario.
#Deberá pedirle su nombre y contraseña.
#Para asegurarnos que no escribe mal la contraseña se le
#pedirá que ingrese su contraseña dos veces. Mientras que las dos contraseñas
#no coincidan se le debe pedir que ingrese la contraseña.

nombre=input("Introduce tu nombre: ")
pass1=input("Introduce una contraseña: ")
pass2=input("Repita la contrasena: ")
while pass1!=pass2:
    print("ERROR, las contrasenas no coinciden")
    pass1=input("Introduce una contraseña: ")
    pass2=input("Repita la contrasena: ")