#Crea una función que obtenga la sumatoria de una lista de números.
#(int[]: nums) => (int: sumatoria)


def sumatorio(nums):
        suma=sum(nums)  #funcion de python que hace sumatorio
        return suma

nums=[1,2,3,4,5]
suma=sumatorio(nums)
print("El sumatorio de numeros es: ",suma)