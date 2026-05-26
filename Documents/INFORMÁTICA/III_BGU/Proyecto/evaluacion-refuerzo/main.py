def menu():
    print("===== MENÚ DE EJERCICIOS =====")
    print("1. Producción de leche")
    print("2. Sueldo semanal")
    print("3. Conversión de metros a pulgadas")
    print("4. Cálculo de edad")
    print("5. Descuento e IVA")
    print("6. Ahorro anual")
    print("0. Salir")


while True:
    menu()

    opcion = int(input("Seleccione una opción: "))

    match opcion:

        case 1:
            pass

        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

        case 6:
            pass

        case 0:
            print("Programa finalizado.")
            break

        case _:
            print("Opción no válida.")