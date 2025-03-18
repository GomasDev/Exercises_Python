"""Ejercicio 42. Crea una lista con palabras. Crea una
segunda lista que contenga sólo las palabras que empiezan por a."""


palabras = ["pepe", "albondiga", "sexo", "gominola"]
palabras_nueva = [palabra for palabra in palabras if palabra[0] == "a"]
print(palabras_nueva)