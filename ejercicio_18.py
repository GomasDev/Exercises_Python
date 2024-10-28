#Crea un programa que calcule el precio final de un pedido en función de
#la cantidad comprada. Supón que el precio de cada artículo es 8.75€:
#Si compras 1-10 unidades, no hay descuento.
#Si compras 11-50 unidades, el descuento es del 5%.
#Si compras 51-100 unidades, el descuento es del 10%.
#Si compras más de 100 unidades, el descuento es del 15%.

cantidad = int(input("¿Cuántos productos has comprado? "))
precio = 8.75
if cantidad >= 1 and cantidad <= 10:
    total = precio * cantidad
elif cantidad >10 and cantidad <= 50:
    descuento = cantidad * precio * 0.05
    total = cantidad * precio - descuento
elif cantidad > 50 and cantidad <= 100:
    descuento = cantidad * precio * 0.1
    total = cantidad * precio - descuento
else:
    descuento = cantidad * precio * 0.15
    total = cantidad * precio - descuento

print(f"Tienes que pagar {total}€")