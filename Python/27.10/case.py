def evaluar_numero(numero):
    match numero:
        case 1:
            return "El numero es uno"
        case 2:
            return "El numero es dos"
        case 3:
            return "El numero es tres"
        case _:
            return "El numero no es uno, dos o tres"
        
resultado = evaluar_numero(2)
print(resultado)

opcion = int(input("Ingrese una opcion (1-4): "))
match opcion:
    case 1:
        print("Opcion 1 seleccionada")
    case 2:
        print("Opcion 2 seleccionada")
    case 3:
        print("Opcion 3 seleccionada")
    case 4:
        print("Opcion 4 seleccionada")
    case _:
        print("Opcion no valida")

print("--- Calculadora ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

operacion = int(input("Seleccione una operacion del (1-4)"))
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

match operacion:
    case 1:
        print("Resultado: ", num1 + num2)
    case 2:
        print("Resultado: ", num1 - num2)
    case 3:
        print("Resultado: ", num1 * num2)
    case 4:
        if num2 !=0:
            print("Resultado: ", num1 / num2)
        else:
            print("Error: Division por 0")
    case _:
        print("Operacion NO valida")

dia = int(input("Ingrese un numerp del 1 al 7 para el dia de la semana: "))
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Numero NO valido para un dia de la semana")

nota = float(input("Ingrese una nota entre 0 a 5: "))
match nota:
    case n if 1 <= n < 3:
        print("Reprobado")
    case n if 3 <= n < 4:
        print("Aprobado")
    case n if 4 <= n < 5:
        print("Exelente")
    case _:
        print("NO es valido")    


