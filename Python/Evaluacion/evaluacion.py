print("==" * 50)
print("EJERCICIO 1")
base= int(input("Cuál es la base del rectangulo:"))
altura= int(input("Cuál es la altura del rectangulo:"))
area = base*altura
perimetro = 2*(base+altura)
print(f"El área del rectángulo es: {area} y el perímetro es: {perimetro}")
print("==" * 50)
print("EJERCICIO 2")
va1 = int(input("Dime un número: "))
va2 = int(input("Dime otro número: "))
va3 = int(input("Dime un último número: "))
media = (va1 + va2 + va3) / 3
print(f"La media de los números es: {media}")
print("==" * 50)
print("EJERCICIO 3")
exa1 = float(input("Dime la nota del primer examen: "))
exa2 = float(input("Dime la nota del segundo examen: "))
exa3 = float(input("Dime la nota del tercer examen: "))
exa = (exa1 + exa2 + exa3) * 0.55
exafin = float(input("Dime la nota del examen final: "))
exafin = exafin * 0.30
trafin = float(input("Dime la nota del trabajo final: "))
trafin = trafin * 0.15
notafinal = exa + exafin + trafin / 3
print(f"La nota final del estudiante es: {notafinal}")
print("==" * 50)
print("EJERCICIO 4")
edad = int(input("Dime tu edad: "))
if edad >= 60:
    print("el precio de tu entrada es de $12.000")
elif edad <= 12:
    print("el precio de tu entrada es de $10.000")
else:
    print("el precio de tu entrada es de $15.000")
print("==" * 50)
print("EJERCICIO 5")
x = int(input("Dame un lado del triangulo: "))
y = int(input("Dame otro de los lados del triangulo: "))
z = int(input("Dame el ultimo lado del triangulo: "))
if x == y == z:
    print("El triangulo es equilatero.")
elif x == y or x == z:
    print("El truangulo es isoceles.")
else:
    print("El triangulo es escaleno.")
print("==" * 50)
print("EJERCICIO 6")
nombre = str(input("Cual es tu nombre: "))
print(f"!Hola {nombre}¡")
print("==" * 50)
print("EJERCICIO 7")
nomco = str(input("Cual es tu nombre completo?: "))
print(nomco.lower())
print(nomco.upper())
print(nomco.title())
print("=="*50)
print("EJERCICIO 8")
prival = int(input("Digite el Primer valor: "))
segval = int(input("Digite el segundo valor: "))
suma = 0 
for i in range(min(prival,segval),max(prival,segval) + 1):
    suma += i
print(f"La suma suma de los numeros desde {prival}, hasta {segval}, es : {suma}.")