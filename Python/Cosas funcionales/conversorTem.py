def conversor_temperatura():
    print("Formatos disponibles: Celsius (C), Fahrenheit (F), Kelvin (K)")

    origen = input("Convertir de (C/F/K): ").upper()
    destino = input("Convertir a (C/F/K): ").upper()
    try:
        temp = float(input("Temperatura a convertir: "))

        if origen == destino:
            print(f"Resultado: {temp}°{destino}")
            return

        # Convertimos primero a Celsius
        if origen == 'F':
            temp_c = (temp - 32) * 5/9
        elif origen == 'K':
            temp_c = temp - 273.15
        elif origen == 'C':
            temp_c = temp
        else:
            print("Unidad de origen no válida.")
            return

        # Convertimos de Celsius al destino
        if destino == 'F':
            resultado = (temp_c * 9/5) + 32
        elif destino == 'K':
            resultado = temp_c + 273.15
        elif destino == 'C':
            resultado = temp_c
        else:
            print("Unidad de destino no válida.")
            return

        print(f"Resultado: {resultado:.2f}°{destino}")
    except ValueError:
        print("Temperatura no válida.")

conversor_temperatura()
