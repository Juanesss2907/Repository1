from datetime import datetime

def calculadora_edad():
    while True:
        fecha_nacimiento = input("Ingresa tu fecha de nacimiento (formato: dd/mm/aaaa): ")
        
        try:
            nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            hoy = datetime.today()

            # Calcular edad en años, meses, días (aproximados)
            edad_dias = (hoy - nacimiento).days
            edad_años = edad_dias // 365
            edad_meses = (edad_dias % 365) // 30
            dias_restantes = (edad_dias % 365) % 30

            print(f"\nTienes aproximadamente {edad_años} años, {edad_meses} meses y {dias_restantes} días.")
            break  # Salimos del bucle si todo fue correcto
        except ValueError:
            print("Fecha no válida. Asegúrate de usar el formato dd/mm/aaaa.\n")

calculadora_edad()


