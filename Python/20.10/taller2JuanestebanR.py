print("----" * 30)

# ejercicio 1
valore = [5,8,9,12,36,9.5]
lista = []
cuadrado = [valore ** 2 for valore in valore]
lista.append(cuadrado)
print(lista)

print("----" * 30)

# ejercicio 2
valores = [5,8,9,12,36,9.5,10]
lista1 = []
valores_pares = [n for n in valores if n % 2 == 0]
lista1.append(valores_pares)
print(lista1)

print("----" * 30)

# ejercicio 3
temperatura_fahrenheit = [32, 212, 275]
lista2 = []
Celsius = [(temperatura_fahrenheit - 32) * (5/9) for temperatura_fahrenheit in temperatura_fahrenheit]
lista2.append(Celsius)
print(lista2)

print("----" * 30)

# ejercicio 4
mi_set = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_2.union(mi_set)
print(mi_set_3)

print("----" * 30)

# ejercicio 5
import random
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
nombreE = random.choice(list(sorteo))
sorteo.remove(nombreE)
print(sorteo)

print("----" * 30)

# ejercicio 6
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damian")
print(sorteo)

print("----" * 30)

# ejercicio 7
prueba = 57 < 77
print("resultado de la comparacion:", prueba)

print("----" * 30)

# ejercicio 8
resultado = 17834/34 > 87*56
print("resultado:", resultado)

print("----" * 30)

# ejercicio 9
raiz = (25**0.5)==5
print(raiz)

print("----" * 30)

# ejercicio 10
## palabra [4]

print("----" * 30)

# ejercicio 11
## Los booleanos true or false

print("----" * 30)

# ejercicio 12
## Listas, porque los set solo aceptan elementos inmutables