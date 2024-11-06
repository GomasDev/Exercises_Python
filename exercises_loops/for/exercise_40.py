#Crea un programa calcule el número de veces que aparece
#dicha letra en el texto.

letra=input("Introduce un letra: ")
texto="Hola a todos buenos dias"
count=0

for n in texto:
    if letra==n:
        count=count+1

print(count)