for x in range (10):
    print(x)

for x in range (100,200):
    print(x)

for x in range (5,20,3):
    print(x)

n=int(input("Ingrese numero: "))
for x in range (n,n*2):
    print(x)

c=int(input("Ingrese numero"))
total=0
for x in range (c):
    numero=int(input("Numero: "))
    total+=numero
    print("Total de la suma", total)

frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiouAEIOU":
    if x in frase:
        print(x)


frase=input("Frase: ")
cantidad=0
for x in frase:
    if x in "aeiou":
        cantidad+=1
        print("Cantidad de vocales", cantidad)

