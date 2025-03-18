#Crea una función que obtenga el máximo de una lista de números.
#No  está permitido el uso de la función preci_max(). (int[]: nums) => (int: máximo)

def maxList(nums):
    maximo=nums[0]
    for i in nums:
        if(i>maximo):
            maximo=i #sobreescribimos el valor de maximo ya que i era mayor
    return maximo

nums=[4,2,1,5,2,6,3,]
maximo=maxList(nums) #llamo a la funcion
print("El numero maximo de la lista es: ",maximo)