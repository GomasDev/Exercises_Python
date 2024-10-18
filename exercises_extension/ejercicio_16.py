#Crea una función que cuenta la cantidad de números pares de una lista
#de números. (int[]: lista_nums) => (int: n_pares)

def count_num_pares(lista_nums):
    suma=0
    for num in lista_nums:
        if num%2==0:
            suma+=num
    return suma


lista_nums=[1,2,3,4,5]

suma_pares=count_num_pares(lista_nums)
print("La suma de los numeros pares es: ",suma_pares)