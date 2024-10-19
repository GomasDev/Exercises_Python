#Crea un programa que solicite al usuario su edad y luego imprima
#  un mensaje que clasifique su etapa de vida:
#  “Bebé (0, 2 años)”, "Niño" (3-12 años), “Adolescente" (13-17 años),
#  "Adulto pero no" (18-34 años), "La mejor edad posible" (35), “Adulto 36-50”,
#  “pre-anciano 51-67”, “Anciano 68-99”, “100 centenario”.

edad=int(input("Introduce tu edad: "))

if 2>=edad>=0:
    print("Eres un bebe")
elif 3<=edad<=12:
    print("Eres un Niño")
elif 13<=edad<=17:
    print("Eres un adolescente")
elif 18<=edad<=34:
    print("Adulto pero no")
elif edad==35:
    print("La mejor edad posible")
elif 36<=edad<=50:
    print("Eres un adulto")
elif 51<=edad<=67:
    print("Eres un preanciano")
elif 68<=edad<=99:
    print("Eres un anciano")
else:
    print("Eres un centenario")