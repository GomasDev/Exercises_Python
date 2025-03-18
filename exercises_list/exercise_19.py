#Ejercicio 19. Crea una lista llamada nombres con los valores ["Ana", "Carlos", "Lucía"].
# Usa insert() para agregar "Beatriz" entre "Ana" y "Carlos"
# Usa insert() para agregar "Diego" al final de la lista. Imprime la lista después de
# cada operación.

lista = ["Ana", "Carlos", "Lucia"]
nombre = "Beatriz"

print(lista)

lista.insert(1, nombre)

print(lista)

nombre2 = "Diego"
lista.insert(len(lista), nombre2)
print(lista)