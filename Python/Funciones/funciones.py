texto = "Esto es un texto de prueba"
resultado = texto.upper()
print(resultado)

texto = "Esto es un texto de prueba"
resultado = texto.lower()
print(resultado)

texto = "Esto es un texto de prueba"
resultado = texto.split("o")
print(resultado)

texto = "Esto es un texto de prueba"
resultado = texto.split("e")
print(resultado)

a = "aprender "
b = "programar "
c = "en ptyhon"
d = "".join([a, b, c])
print (d)

tezto = "  Esto es un texto de prueba   "
resultado = texto.strip()
print(resultado)

texto = "Esto es un texto de prueba"
resultado = texto.replace("a", "@")
print(resultado)

texto = "Esto es un texto de prueba"
resultado = texto.find("t")

#propiedades de string: Son inmutables no pueden cambiar su orden interno ni alterar su contenido concatenable mi_texto="hola" + mundo multipicable mi_texto = "hola" * 5. Multilineales mi_texto"hola/mundo" se puede hacer usando """", verificar si contiene: uno dentro de otro (tru-false), calcular longirud mi_texto = "hola mundo" len(mi_texto) mi_texto ="hola mundo" mi texto [0:3], mi_texto[;;-1] ,mi_texto.replace("hola" ,"adios")

text1 = "Hola"
text2 = "mundo"
text3 = text1 + "" + text2
print (text3)

text4 = text1 * 5
print(text4)

text5 = """esto es un
salto de linea"""
print(text5)

#longitus string
print(len(text5))

text6 = "Esto es un texto de prueba"
print("multilinea\n", text6)

text7 = "Hola mundo"
print(text7[0:3])

text8 = "Hola mundo"
print("Hola" in text8)
print("adso" in text8)

name = input ("¿Cuál es tu nombre?: ")
print(name.lower())
print(name.upper())
print(name.strip())
print(name.title()) #Primera de la oración en mayúscula
print(name.capitalize()) #Primera letra de cada palabra en mayúscula