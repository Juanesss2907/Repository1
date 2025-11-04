# ejercicio 1
mi_dic = {"nombre":"Karen", "apellido":"Solis", "edad":35, "Ocupacion":"Perdiodista"}
print(type(mi_dic))
print(mi_dic)

print("___"*50)

# ejercicio dos
mi_dic2 = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,
300,15]}}
print(mi_dic2["puntos"] ["points2"] [1])

print("___"*50)

# ejercicio 3
mi_dic = {"nombre":"Karen", "apellido":"Solis", "edad":35, "ocupacion":"Perdiodista"}
mi_dic["ocupacion"] = "editora"
mi_dic["pais"] = "colombia"
mi_dic["edad"] = 36
print(mi_dic)

print("___"*50)

# ejercicio 4
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(f"El numero 2 aparece {mi_tupla.count(2)} veces")
print(f"El numero 3 aparece {mi_tupla.count(3)} veces")
print(f"El numero 1 aparece {mi_tupla.count(1)} veces")

print("___"*50)

# ejercicio 5
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
lista = list(mi_tupla)
print(lista)

print("___"*50)

# ejercicio 6
mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
print(a)    
print(b)    
print(c)
print(d)    

print("___"*50)

# ejercicio 7
lista = []

for i in range(5):
    valor = int(input("Introduce un número entero: "))
    lista.append(valor)

lista_invertida = lista[::-1]

print("Elementos en orden inverso:")
for i in lista_invertida:
    print("Valor: %d" % i)

