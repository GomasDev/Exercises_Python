#Crea un programa que calcule el impuesto sobre la
#renta de una persona según los siguientes tramos impositivos:
#Ingresos ≤ 10,000: 0% de impuesto
#Ingresos > 10,000 y ≤ 20,000: 10% de impuesto sobre el exceso de 10,000
#Ingresos > 20,000 y ≤ 40,000: 10% sobre los primeros 10,000 y 20% sobre el exceso de 20,000
#Ingresos > 40,000: 10% sobre los primeros 10,000, 20% sobre el exceso de 20,000 y 30% sobre el exceso de 40,000


ingresos=float(input("Introduce los ingresos: "))

if ingresos <= 10000:
        impuesto = 0
elif ingresos <= 20000:
        exceso = ingresos - 10000
        impuesto = exceso * 0.10
elif ingresos <= 40000:
        exceso1 = ingresos - 20000
        impuesto = (10000 * 0.10) + (exceso1 * 0.20)
else:
        exceso2 = ingresos - 40000
        impuesto = (10000 * 0.10) + (20000 * 0.20) + (exceso2 * 0.30)

print("El impuesto sobre la renta es: ", round(impuesto, 2))