#Crea un programa en el cual el usuario
#inserta un año y el programa le devuelve el siglo del año.

ano = int(input("Inserta un año: "))
if ano % 100 == 0:
    siglo = ano // 100
else:
    siglo = ano // 100 + 1

print(f"El año {ano} pertenece al siglo {siglo}")