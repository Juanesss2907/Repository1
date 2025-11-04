# 1. Crear lista con 5 elementos
mi_lista = ["Juanes", 777, "Ruiz", 27.7, "Algoritmos"]
print("Mi lista:", mi_lista)

# 2. Agregar "motocicleta" a la lista de medios de transporte
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print("Medios de transporte:", medios_transporte)

# 3. Usar pop() para quitar el tercer elemento de la lista de frutas
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2) 
print("Lista de frutas después de pop:", frutas)
print("Elemento eliminado:", eliminado)

# 4. Crear lista de números y mostrar el valor 90
lista_numeros = [10, 46, 78, 90, 102, 104]
print("El valor en la lista es:", lista_numeros[3])

# 5. Ordenar lista de números de mayor a menor
lista_numeros2 = [10, 45, 356, 16, 25, 18, 46, 67, 49, 98, 106, 43, 120, 65, 80]
lista_numeros2.sort(reverse=True)
print("Lista ordenada de mayor a menor:",lista_numeros2)