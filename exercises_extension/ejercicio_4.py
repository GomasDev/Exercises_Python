#Crea una función que determine si una cadena de texto es un palíndromo.
# (string: palabra) => (boolean: es_palindromo)

def palindromo(texto):
    texto_limpio = ''.join(letra.lower() for letra in texto if letra.isalnum()) #letra.lower() convierte las letras en minusculas,
                                                                                #para que no afecte al resultado
    return texto_limpio==texto_limpio[::-1]

texto="Hola me llamo juan"
texto2="Anita lava la tina"
print(texto)
print(palindromo(texto))
print(texto2)
print(palindromo(texto2))

