#27. Crea una función que imprima el siguiente ‘mosaico’:
#1
#22
#333
#4444
#55555
#666666
#(int:n) => void. Siendo n el número de líneas, en el ejemplo anterior n = 6.

def mosaico(n):
    for i in range(1,n+1):
        print(str(i)*i)

tamaño=int(input("Tamañp de mosaico: "))
mosaico(tamaño)