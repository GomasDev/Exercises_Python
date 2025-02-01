#Ejercicio 9. Crea un programa que simule el juego “pares o nones”.
# Primero eliges entre pares o nones y después eliges cuantos dedos sacas.
# A continuación la máquina decide, de forma aleatoria, cuántos dedos saca
# y se comprueba quién ha ganado.


import random


while True:
    try:

        print("=== JUEGO PARES O NONES ===")
        opcion=int(input("Elige entre pares(1) o nones(2): "))
        if opcion not in [1,2]:
            print("Opcion no valida.")
            continue

        dedos=int(input("Elige cuantos dedos sacas: "))
        if dedos not in range(0,10):
            print("Opcion no valida (0-10).")
            continue

        eleccionMaquina = random.randint(0, 10)
        print(f"La maquina ha elegido {eleccionMaquina} dedos.")

    except ValueError as error:
        print(f"ERROR: {error}")
    except Exception as error:
        print(f"ERROR: {error}")

    else:
        total=dedos+eleccionMaquina
        print(f"Total de dedos: {total}")
        if total%2==0:
            if opcion==1:
                print("Has ganado!")
            else:
                print("Has perdido!")
        else:
            if opcion==2:
                print("Has ganado!")
            else:
                print("Ha ganado la maquina")

        jugar_otravez=input("Quieres jugar de nuevo? (s/n): ").strip().lower()
        if jugar_otravez!="s":
            break