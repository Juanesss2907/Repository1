def calculadora():
    print("Operaciones disponibles: suma (+), resta (-), multiplicación (*), división (/)")
    
    try:
        num1 = float(input("Ingresa el primer número: "))
        operador = input("Ingresa el operador (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Error: No se puede dividir entre cero.")
                return
        else:
            print("Operador no válido.")
            return

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Por favor, ingresa números válidos.")

calculadora()
