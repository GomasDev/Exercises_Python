#Crea un programa que pida al usuario su calificación numérica (de 0 a 100)
#  y muestre su equivalente en letra (sistema de calificación de EEUU):
#  A → 90 -100, B → 80 - 89, C → 70 - 79, D → 60-69 y F → menos de 6

clasificacion=int(input("Introduce un clasificacion numerica(0-100): "))

if 0<clasificacion<=100:
    if clasificacion>=90:
        print("A->90-100")
    elif clasificacion>=80:
        print("B->80-89")
    elif clasificacion>=70:
        print("C->70-79")
    elif clasificacion>=60:
        print("D->60-69")
    elif clasificacion<60:
        print("F->menos que 60")
else:
    print("La clasificacion numerica no es valida")