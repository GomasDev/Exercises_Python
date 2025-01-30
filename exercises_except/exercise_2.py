"""Ejercicio 2. Crea un programa que convierta temperaturas. El usuario debe ingresar
una temperatura y la escala original (Celsius o Fahrenheit) y el programa la
convertirá a la otra escala."""


def cambio(grados: float, escala: str) -> float:
    if escala.lower() == "celsius":
        if grados < -273.15:
            raise ValueError("La temperatura en Celsius no puede ser menor a -273.15°C.")
        return grados * 9 / 5 + 32
    elif escala.lower() == "fahrenheit":
        if grados < -459.67:
            raise ValueError("La temperatura en Fahrenheit no puede ser menor a -459.67°F.")
        return (grados - 32) * 5 / 9
    else:
        raise ValueError("Escala no reconocida. Use 'Celsius' o 'Fahrenheit'.")


def main():
    print("=== Conversor de Temperaturas ===")
    try:
        grados = float(input("Ingrese la temperatura: "))
        escala = input("Ingrese la escala (Celsius o Fahrenheit): ").strip()
        nueva_temperatura = cambio(grados, escala)
    except ValueError as error:
        print(f"ERROR: {error}")
    else:
        if escala.lower() == "celsius":
            print(f"{grados}°C son {nueva_temperatura:.2f}°F.")
        elif escala.lower() == "fahrenheit":
            print(f"{grados}°F son {nueva_temperatura:.2f}°C.")


if __name__ == "__main__":
    main()
