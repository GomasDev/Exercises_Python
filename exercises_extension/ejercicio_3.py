# Crea una función que dada una distancia en millas calcule su  correspondiente en kms.
# Los parámetros (int: distancia_millas) => (int: distancia_kms)

def distancia_millas(distancia_kms):
    millas=distancia_kms*0.621371
    return millas

distancia_kms=float(input("Introduce la distancia en km: "))
millas=distancia_millas(distancia_kms)
print("La distancia en millas es: ",millas)