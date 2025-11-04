from random import *

#1
print("Numeros del 20 al 40:")
for numero in range (20, 41):
    print(numero)

#2
print("Lista de numeros del 30 al 50 con paso 2:")
lista_numeros = list(range(30, 51, 2))
print(lista_numeros)

#3
print("Usando enumerate para obtener indice y valor:")
lista = ["a", "b", "c", "d"]
for indice, valor in enumerate(lista):
    print(f"Indice: {indice}, Valor: {valor}")

#4
print("Ejemplo dos enumerate:")
lista1 = ["a", "b", "c", "d", "e"]
for item in enumerate(lista1):
    print(item)

#5
lista2 = ["x", "y", "z"]
tupla_enumerada = tuple(enumerate(lista2))
print("Tupla con indice y valor:", tupla_enumerada)

#6
lista_nombres = ["Juanes", "Nicko", "Steven"]
lista_edades = [19, 30, 28]
lista_ciudades = ["Suecia", "Italia", "Belgica"]
combinado = list(zip(lista_nombres, lista_edades, lista_ciudades))
for nombre, edad, ciudad in combinado:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

#7
menor = min(78, 56, 89, 23, 45)
mayor = min(78, 56, 89, 23, 45)
print(f"El menor es: {menor}")
print(f"El mayor es: {mayor}")

#8
lista = [12, 45, 7, 23, 89, 34]
print(max(lista))
print(min(lista))

#9
nombre = ["Isabella", "Juanes", "Nicko", "Steven"]
print("Nombre menor alfabeticamente:", min(nombre))
print("Nombre mayor alfabeticamente:", max(nombre))

#10
cadena = "Python"
print("Caracter minimo en 'Python':", min(cadena))
print("Caracter maximo en 'Python':", max(cadena))

#11
nom = "Juanes"
print("Caracter minimo en 'Juanes':", min(nom))
print("Caracter maximo en 'Juanes':", max(nom))

#12
diccionario = {'a': 5, 'b': 2, 'c': 8}
print("Clave minima en diccionario:", min(diccionario)) 
print("Clave maxima en diccionario:", max(diccionario)) 
print(min(diccionario.values()))
print(max(diccionario.values()))

#13
num_aleatorio = randint(1, 100)
print("Numero aleatorio entre 1 y 100:", num_aleatorio)

#14
aleatorio_flotante = uniform(1.0, 10.0)
print("Numero flotante aleatorio entre 1.0 y 10,0:", aleatorio_flotante)

#15
aleatorio_0_1 = random()
print("Numero aleatorio entre 0.0 y 1.0", aleatorio_0_1)

#16
colores = ["Rojo", "Azul", "Negro", "Morado"]
color_seleccionado = choice(colores)
print("Color seleccionado aleatoriamente:", color_seleccionado)

#17
numeros = [1, 2, 3, 4, 5]
print("Lista original de numeros:", numeros)
shuffle(numeros)
print("Lista de numeros mezclada:", numeros)