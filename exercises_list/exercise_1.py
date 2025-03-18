#Ejercicio 1. Crea una lista con las provincias de Andalucía
# y muestra por pantalla solo aquellas
# que empiezan por la letra C.


andalucia=["Huelva", "Granada", "Sevilla", "Cadiz", "Jaen", "Almeria", "Cordoba"]

for i in andalucia:
    if i[0].lower()=="c":
        print(i)