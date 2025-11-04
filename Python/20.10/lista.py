#1
palabra = "Python"
lista_tradicional = []
for letra in palabra:
    lista_tradicional.append(letra)
print("Lista tradicional:", lista_tradicional)

#2
palabra = "Python"
lista_comprension = [letra for letra in palabra]
print("Lista por comprension:", lista_comprension)

#3
lista1 = [caracter for caracter in "Python"]
print("Otra lista por comprension:", lista1)

#4
listnum = [n for n in range(0, 21, 2)]
print("Lista numeros pares:", listnum)

#5
pies =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
metros = [round(pie * 0.3048, 4) for pie in pies]
print("Pies a metros:", metros)

#6
celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fahrenheit = [round((temp * 9/5) + 32, 2) for temp in celsius]
print("Celsius a fahrenheit:", fahrenheit) 