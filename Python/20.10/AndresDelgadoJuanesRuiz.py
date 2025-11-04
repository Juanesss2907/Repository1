# Juan Esteban Ruiz Quintero y Andres Felipe Delgado 

print("Buenos días querido profesor.")
texto_cualquiera = input("Escribe un texto de tu preferencia: ").lower()
pal = texto_cualquiera.split()
numpal = len(pal)

letras = []

letra1 = input("Escribe una letra a azar: ").lower()
letra2 = input("Escribe otra letra: ").lower()
letra3 = input("Escribe la ultima letra: ").lower()

letras.append(letra1)
letras.append(letra2)
letras.append(letra3)

numletra1 = texto_cualquiera.count(letra1)
numletra2 = texto_cualquiera.count(letra2)
numletra3 = texto_cualquiera.count(letra3)

print(f"El numero de {letra1} en el texto es {numletra1}, el numero de {letra2} en el texto es {numletra2}, y de {letra3} es {numletra3}.")
 
print(f"El numero de palabras del texto es : {numpal}")

primera_letra = texto_cualquiera[0]
ultima_letra = texto_cualquiera[-1]

print(f"La primera letra del texto {primera_letra}, la ultima letra del texto es {ultima_letra}.")

texto_inverso = texto_cualquiera[::-1]

print(f"Texto invertido:{texto_inverso}.")