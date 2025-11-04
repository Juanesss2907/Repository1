# conjunto set #
#
# un set almacena elementos unicos
# no tiene orden ni idices (no se puede acceder por indice[i])
# los elementos son inmutables (no se pueden cambiar)
# de pueden agregar o eliminar elementos
#
## crear set desde una lista ##
## duplicados se eliminan automaticamente ##
lista_con_duplicados = [1,2,3,4,4,5]
set_desde_lista = set(lista_con_duplicados)
print("set desde lista (sin duplicados)",set_desde_lista)

#crear set desde un string
nombres = ["ana","luis","maria","ana","carlos"]
sin_duplicados = set(nombres)
print("set desde lista de nombres (sin duplicados):",
      sin_duplicados)

## literal set con llaves
otro_set = {10,20,30,20,10}
print("set creado con llaves (sin duplicado):", otro_set)
print("tipo de dato: ",type(otro_set))

#### operaciones basicas ####
set_a = {1,2,3,4}
set_b = {3,4,5,6}
# union: elementos A o B
union_set = set_a.union(set_b)
# se pueden incluir tuplas son inmutables
mi_set3 = set([1, 2(2,3,4),5,6])
print("set con tupla incluida: ", mi_set3)

##mutaciones: add, remove, pop, clear ##
set4 = set([1,2,3])
set4.add(4) #agregar elemento
print("set despues de add(4):", set4)
set4.remove(2) #eliminar elemento 2
print("set despues de remove(2): ", set4)
eliminado = set4.pop() #elimina y retorna un elemento aleatorio
print("elemento eliminado con pop():",eliminado)
print("set despues de pop():",set4)
set4.clear() # elimina todos los elementos
print("set despues de clear():",set4)