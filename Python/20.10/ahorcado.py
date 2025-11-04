from random import choice

palabras = ['celular', 'programacion', 'videojuegos']
letras_correctas = []
letras_incorrectas = []

intentos = 7
aciertos = 0
juego_terminado = False

def elergir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    return palabra_elegida

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")
    return letra_elegida

def nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta):
    global intentos, aciertos
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        aciertos += palabra_oculta.count(letra_elegida)
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, intenta con otra.")
    else:
        if letra_elegida not in letras_incorrectas:
            letras_incorrectas.append(letra_elegida)
            intentos -= 1
            print("Letra incorrecta. Te quedan", intentos, "intentos.")
        else:
            print("Ya habías intentado esa letra y no está en la palabra.")

def perder(palabra_oculta):
    print("Has perdido. La palabra era:", palabra_oculta)

def ganar(palabra_oculta):
    print("¡Felicidades! Has ganado. La palabra era:", palabra_oculta)

palabra = elergir_palabra(palabras)

while not juego_terminado:
    print("\n")
    nuevo_tablero(palabra)
    print("Letras incorrectas:", ', '.join(letras_incorrectas))
    letra = pedir_letra()

    chequear_letra(letra, palabra)

    if aciertos == len(palabra):
        ganar(palabra)
        juego_terminado = True

    if intentos == 0:
        perder(palabra)
        juego_terminado = True
