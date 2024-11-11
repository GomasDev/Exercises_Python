#Crea un programa que lea palabras hasta que insertes la
#palabra ‘fin’
#. Al finalizar deberá mostrarte la palabra con menos letras y la
#palabra con más letras de todas las que hayas insertado sin tener en cuenta
#la palabra ‘fin’

palabramayor=""
palabramenor=""
i=0
while True:
    palabras=input("Introduce palabras: ")
    if i==1:
        palabramayor=palabras
        palabramenor=palabras
    if len(palabramayor)>len(palabras):
        palabramayor=palabras
    elif len(palabramenor)<len(palabras):
        palabramenor=palabras
    if palabras=="fin":
        break
    i=i+1

print("La palabra mayor es: ",palabramayor)
print("La palabra menor es: ",palabramenor)