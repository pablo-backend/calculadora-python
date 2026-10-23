def calcular(operacion, numero1, numero2):
    if operacion == "1":
        return numero1 + numero2
    if operacion == "2":
        return numero1 - numero2
    if operacion == "3":
        return numero1 * numero2
    if operacion == "4":
        if numero2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return numero1 / numero2
    raise ValueError("La operación elegida no es válida.")


def main():
    print("Calculadora básica")

    while True:
        print("\nElige una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        operacion = input("Opción: ").strip()
        if operacion == "5":
            print("Hasta luego.")
            break
        if operacion not in {"1", "2", "3", "4"}:
            print("Elige una opción del 1 al 5.")
            continue

        try:
            numero1 = float(input("Primer número: "))
            numero2 = float(input("Segundo número: "))
            resultado = calcular(operacion, numero1, numero2)
        except ValueError as error:
            print(f"Entrada no válida: {error}")
            continue
        except ZeroDivisionError as error:
            print(error)
            continue

        print(f"Resultado: {resultado:g}")


if __name__ == "__main__":
    main()