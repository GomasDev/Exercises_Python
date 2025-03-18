alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

suma = 0
n_alumnos = len(alumnos)

for alumno in alumnos:
    suma += sum(alumno[1:])/3

nota_media = suma / n_alumnos
print(f"La nota media de la clase es: {nota_media}")


def dimensiones_matriz(matriz):
    # El número de filas será simplemente el tamaño de la lista de la matriz
    filas = len(matriz)

    # El número de columnas será el tamaño de la primera fila (suposición: la matriz es rectangular)
    columnas = len(matriz[0]) if filas > 0 else 0

    return [filas, columnas]


# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(dimensiones_matriz(matriz))  # Salida: [3, 3]


def pais_con_mayor_densidad(continente, paises):
    mayor_densidad = 0
    pais_densidad_maxima = ""

    for pais in paises:
        if pais[4] == continente:  # Comparamos el continente
            poblacion = pais[2]
            area = pais[5]
            densidad = poblacion / area  # Calculamos la densidad

            if densidad > mayor_densidad:
                mayor_densidad = densidad
                pais_densidad_maxima = pais[0]  # Guardamos el país con mayor densidad

    return pais_densidad_maxima

# Ejemplo de uso
paises = [
    ["Argentina", "Buenos Aires", 46000000, "América", 2780400],
    ["España", "Madrid", 48000000, "Europa", 505990],
    ["Japón", "Tokio", 125000000, "Asia", 377975],
    ["Sudáfrica", "Pretoria", 60000000, "África", 1221037],
    ["Australia", "Canberra", 26000000, "Oceanía", 7692024],
    ["Canadá", "Ottawa", 38000000, "América", 9984670]
]

print(pais_con_mayor_densidad("América", paises))  # Salida: Argentina


def suma_matrices(m1, m2):
    # Comprobamos que ambas matrices tengan las mismas dimensiones
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")

    # Sumamos las matrices
    resultado = []
    for i in range(len(m1)):
        fila_resultado = []
        for j in range(len(m1[0])):
            fila_resultado.append(m1[i][j] + m2[i][j])
        resultado.append(fila_resultado)

    return resultado


# Ejemplo de uso
m1 = [
    [1, 2, 3],
    [4, 5, 6]
]

m2 = [
    [6, 5, 4],
    [3, 2, 1]
]

print(suma_matrices(m1, m2))  # Salida: [[7, 7, 7], [7, 7, 7]]
