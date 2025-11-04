print("Ejercicio 1")
alumnos_clase = ["Maria", "Laura", "Andres", "Lucas", "Juanes", "Elkin", "Valentina"]

for alumno in alumnos_clase:
    print("Hola " + alumno)

print("\n Ejercicio 2")
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_numeros = 0  

for numero in lista_numeros:
    suma_numeros += numero 

print("La suma de los números es:", suma_numeros)

print("\n Ejercicio 3")
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:     
        suma_pares += num
    else:                 
        suma_impares += num

print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)

print("\n Ejercicio 4")
numero = 10  

while numero >= 0:  
    print(numero)
    numero -= 1  

print("\n Ejercicio 5")
mi_lista = list(range(2500, 2586))  

print(mi_lista)

print("\n Ejercicio 6")

mi_lista = list(range(3, 301, 3))
print(mi_lista)

print("\n Ejercicio 7")
suma_cuadrados = 0  

for numero in range(1, 16): 
    cuadrado = numero ** 2   
    suma_cuadrados += cuadrado  

print(suma_cuadrados)

print("\n Ejercicio 8")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

print("\n Ejercicio 9")
lista_indices = list(enumerate("Python"))
print(lista_indices)


print("\n Ejercicio 10")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)
