"""Ejercicio 43. Crea una lista con palabras. Crea una segunda
 lista que contenga las mismas palabras pero con todas sus
 letras en mayúscula."""


palabras = ["pepe", "albondiga", "sexo", "gominola"]
palabras_nueva = [palabra.upper() for palabra in palabras]
print(palabras_nueva)