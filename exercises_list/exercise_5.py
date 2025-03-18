#Ejercicio 5. Utilizando ChatGPT crea una lista de 1000 números aleatorios.
#Muestra por pantalla el menor de los números (utilizando bucles, la gracias
#es que encuentre el menor el ordenador, no tú).

numeros_aleatorios = [
    742, 618, 201, 456, 915, 832, 374, 598, 129, 657,
    843, 234, 908, 371, 502, 3, 167, 291, 620, 854,
    741, 369, 284, 623, 928, 410, 537, 715, 842, 630,
    158, 794, 205, 376, 981, 472, 643, 219, 567, 731,
    302, 451, 689, 825, 914, 508, 390, 611, 874, 267,
    182, 748, 509, 366, 999, 413, 735, 280, 561, 690,
    833, 146, 502, 904, 621, 473, 259, 528, 799, 307,
    711, 951, 369, 582, 463, 850, 124, 777, 320, 591,
    402, 675, 888, 213, 745, 654, 138, 598, 822, 409,
    987, 326, 741, 510, 678, 129, 347, 905, 267, 731
]

menor=numeros_aleatorios[0]
for numero in numeros_aleatorios:
    if menor>numero:
        menor=numero

print(menor)