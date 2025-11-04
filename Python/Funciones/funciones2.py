mi_text = "Esta es una prueba de index"
resultado = mi_text[8]
print(resultado)
#muestra la posición 8 (la U)

mi_text = "Esta es una prueba de index"
resultado = mi_text.index("i")
print(resultado)
#cuenta los caracteres del texto

mi_text = "Esta es una prueba de index"
resultado = mi_text.index("a", 5)
print(resultado)
#el segundo es la posición inicial de busqueda

mi_text = "Esta es una prueba de index"
resultado = mi_text.index("a")
print(resultado)
#ubica la posición de la primera A

texto = "ABCDEFGHIJKLMNOPQ"
fragmento = texto[2:5]
print(fragmento)
#Desde el indice 2 hasta 5 (5 exclusivo): 2,3,4

texto = "ABCDEFGHIJKLMNOPQ"
fragmento = texto[:5]
print(fragmento)
#Desde el inicio hasta 5 (exclusivo): 0..4

texto = "ABCDEFGHIJKLMNOPQ"
fragmento = texto [2:10:2]
print(fragmento)
#desde 2 hasta 10 (10 exclusivo), saltando de 2 en 2: 2,4,6,8.

texto = "ABCDEFGHIJKLMNOPQ"
fragmento = texto[::-2]
print(fragmento)

string = "Python"
#desde indice 0 hasta antes del 2
print(string[0:2])
#desde inicio hasta antes de 4
print(string[:4])
#desde indice 2 hasta el final
print(string[2:])
#de 2 en 2 (0, 2, 4)
print(string[::2])
#al revés
print(string[::-1])

"El sicling en Python es una técnica que permite extraer partes "

x = 10
y = 7
z = 2

#concatenar usando el "+"
#concatenar de forma literal "F"
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} x {y} = {x*y}")
print(f"{x} / {y} = {x/y}")
print(f"{y} con divisón al piso de {z} = {y//z}")
print(f"{7} mod {3} = {y%z}")
print(f"{x} ^2 {2} = {x**2}")
print(f"{x} ^3 {3} = {x**3}")
print(f"2√ de {x} = {x**0.5}")
print(f"división al piso {874} y {27} = {874//27}")

resultado =(round(90/7))
print=(resultado)

resultado=(90/7)
print=(round(resultado))

valor = round (88.7777777)
print=(valor)
#TYPE: le indicaremos el tipo de dato que tendrá la variable
print=(type(valor))
valor = (88.7777777)
print(round(valor))
print=(type(valor))
#se le indicará el número de décimales que mostrará en pantalla
resultado = (10/3)
print(round(resultado,2))

num1 = round(13/2,0)
print(num1)

frase = "Hola, ¿cómo estás?"
resul = frase.replace("Hola, buenos")
result= frase.replace("como","dias")
print(result)