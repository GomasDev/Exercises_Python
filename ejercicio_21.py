#Crea una función que calcule si un número dado es primo o no. (int:n) =>
#(boolean: es_primo)

def primo(num):
    for n in range (2,num):
        if num%n==0:
            return False    
        return True
        
num=int(input("Dime un numero para saber si es primo o no: "))
print(primo(num))