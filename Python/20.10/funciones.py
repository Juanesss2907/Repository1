##Una funcion es un bloque de codigo que se ejecuta solo cuando la llamas
##Sirve para organizar el codigo, evitar repeticiones
#y hacerlo mas facil de entender

#ESTRUCTURA
#def-> palabra clave para definir una funcion
#nombre de la funcion
#parametros o argumnetos -> valores que se le pasan a la funcion (opcionales)
#return -> devuleve un resultado (opcionales)
#En python los funciones juegan un papel crucial al permitirte escribir codigo mas limpio, eficiente y facil de mantener

def saludar():
    print("Hola Leidy")
#para ejecutarla
saludar()

def mensaje():
    print("Estoy aprendiendo python")
mensaje()

#CON PARAMETROS
def saludar(nombre):
    print(f"Hola {nombre}, ¿cómo estás?")
saludar("Leidy")    
saludar("Jhoan")
saludar("Yeral")

#definicion de una funcion sin parametros
def my_function():
    print("Hola, esta es mi primera funcion")
my_function()

#Calculadora
def calculadora(a,b,operacion):
    if operacion == "suma":
        return a+b
    elif operacion == "resta":
        return a-b
    elif operacion =="multiplicacion":
        return a*b
    elif operacion =="division":
        return a/b
    else:
        return "Operacion no valida"
    
op = input("Ingrese la operacion que desea realizar(suma, resta, division, multiplicacion): ")  
num1 = float(input("Ingrese el primero número: "))
num2 = float((input("Ingrese el segundo nimero: ")))
result = calculadora(num1, num2, op)
 
print("El resultado es: ", result)

##FUNCION CON LISTA
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)
mi_lista = [1,2,3,4,5]  
imprimir_lista(mi_lista)      
        
 ##____________________
def multiplicar(numero1, numero2):
     return numero1 * numero2   
multi = multiplicar(5,10)
print("El resultado de la multiplicaciones:", multi)

def chequear_tres_cifras (numero):
    return numero in range(100, 1000)
resultado1 = chequear_tres_cifras(345)
print("¿345 tiene tres cifras?", resultado1)
resultado2 = chequear_tres_cifras(89)
print("¿89 tiene tres cifras?", resultado2)

### lista tupla (producto, precio) ###
precios_cafe = [("espresso",3500),("latte",4000),
                ("cappucino"),5500]
def cafe_mas_caro(lista_precios):
    preciomayor = 0 
    cafe_caro = ' ' 
    for cafe, precio in lista_precios:  
        if precio > preciomayor:
            preciomayor = precio
            cafe_caro = cafe
        else:
            pass
        return cafe_caro, preciomayor
print("el cafe mas caro es: ",cafe_mas_caro(precios_cafe))

## argumentos por defecto ##
def potencia(base, exponente = 2):
    return base ** exponente
print("3 al cuadrado es: ", potencia(3))
print("2 al cubo es: ",potencia(2,exponente=3))

## funcion con dos parametros obligatorios y uno opcional###
def suma(a,b):
    return a + b
print(suma(4,5))
# llama a la funcion con dos argumentos obligatorios

#*args permite recibir una cantidad de argumentos variables
def suma_varios_numeros(*args):
    total = 0
    for numero in args:
        total += numero
        return total 
print("La suma es: ", suma_varios_numeros(1, 2, 3, 4, 5, 6))

#Usando directamente la función sum()
def suma2(*args):
    return sum(args)
print("La suma es: ", suma2(10, 20, 30, 40))

# **kwargs permite recibir argumentos con nombre variables
# kwargs recibe un diccionario como argumento

def suma3(**kawargs):
    print(type(kawargs))
suma3(a=1, b=2, c=3)
# llama la funcioncion con argumentos nombrados variables

def suma4(**kawargs):
    for clave, valor in kawargs.items():
        print(f"{clave}  = {valor}")
suma4(x=10, y=20, z=30)

def suma5(**kawargs):
    total = 0
    for clave, valor in kawargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total
print("La suma es:", suma5(a=5, b=15, c=25))

def funcion_combinada(param1, param2, *args, **kawargs):
    print("Parametro 1:", param1)
    print("Parametro 2:", param2)
    print("Argumentos adicionañes (args):", args)
    print("Argumentos nombrados adicionales (kawargs):", kawargs)
funcion_combinada(1, 2, 3, 4, 5, nombre="Ana", edad=30)

    
    