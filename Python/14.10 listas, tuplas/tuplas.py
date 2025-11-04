"""Las tuplas son colecciones ordenadas e inmutables es decir, una vez creadas no se pueden modificar (no se pueden agregar, eliminar o cambiar elementos)
Se definen usando parentesis() pueden contener elementos de diferentes tipos de datos. Son utiles para almacenar datos que no deben cambiar como coordenadas geográficas, fechas, etc. Para proteger datos de modificaciones accidentales.
Caracteristicas: Ocupan menos espacio en memoria que las listas son más rápidas que las listas para ciertas operaciones pueden tener diferentes tipos de datos se pueden anidar"""

#Ejemplo básico de una tupla
mi_tuple = (1, 2, 3, 4)
print(type(mi_tuple))
print(mi_tuple)
print(len(mi_tuple))

#Ejemplo de tupla con diferentes tipos de datos
mi_tuple1 = (1, "hola", 3.14 ,True)
print(type(mi_tuple1))
print(mi_tuple1)

tupla=(1, 2, 3, 4, 5)
print(tupla[0]) #acceder al primer elemento
print(tupla[1:4]) #acceder a una porción de la tupla
print(tupla[-1]) #acceder al último elemento

#Tuplas aninadas
tupla_aninada=(1, 2, (3, 4), (5, 6))
print(tupla_aninada[2]) #acceder a la tupla (3, 4)

#Intentar modificar una tupla genera un error
#Este código generará un error
"""tuple2=(1, 2, 3)
tuple2[0]=10 #Esto genera un error
print(tuple2)"""

#Operaciones con tuplas
tupla1=(1, 2, 3)
tupla2=(4, 5, 6)
tupla3=tupla1+tupla2 #Concatenación de las tuplas
print(tupla3)
print(tupla3.count(2)) #Contar cuantas veces aparece el valor 2
print(tupla3.index(5)) #Encontrar la posición del valor 5

#Desempaquetado de tuplas
tupla4 = (10, 20, 30)
a, b, c = tupla4
print(a)    #10
print(b)    #20
print(c)    #30
print(len(tupla4))

#Tuplas con un solo elemento
tupla5=(100,) #Nota la coma al final
print(type(tupla5)) #Es una tupla
print(tupla[0])    #100

#Sin la coma sería un entero
tupla6=(100) #Sin la coma

#Métodos de tuplas
t=(1,2,3,4,5,1)
print(t.count(1)) #Cuantas aparece el 1
print(t.index(3)) #En que posición está el 3
print(3 in t) #Verificar si el 4 está en la tupla

#Iterar sobre una tupla
tupla7=("a", "b", "c")
for elemento in tupla7:
    print(elemento)

#Repetir una tupla
tupla8=(1, 2)
tupla9=tupla8*3
print(tupla9)    #(1, 2, 1, 2, 1, 2)

#Convertir una lista en tupla
mi_lista=[1, 2, 3]
mi_tupla=tuple(mi_lista)

#Comprobar si un elemento está en la tupla
tupla10 = (10, 20, 30)
if 30 in tupla10:
    print("30 está en la tupla")
else:
    print("30 NO está en la tupla")

#Crear una tupla con datos y mostrando formateados
persona = ("Juan", 25, "Manizales")
print(f"Nombre: {persona[0]}, Edad: {persona[1]}, ciudad: {persona[2]}")