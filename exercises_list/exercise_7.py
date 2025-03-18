#Ejercicio 7. Crea una variable con tu nombre completo (nombre + apellidos) y
#muestra por pantalla, en orden de aparición, las vocales que hay en tu
#nombre completo.


nombre = "Rafael Ballesteros"
vocales= ["a", "e", "i", "o", "u"]

for vocal in nombre:
    if vocal.lower() in vocales:
        print(vocal)