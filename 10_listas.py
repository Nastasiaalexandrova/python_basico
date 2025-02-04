"""
LISTAS
"""

# las listas en Python equivalen alos "arrays" de otros lenguajes
# las listas y los string son "iterables"
# la separacion con comas
# la lista es una coleccion de datos indexada

lista = [1, 2, 3, 4, 5]
lista_nombres = ["Maria", "Pau", "Pol"]
lista_mixta = [1, "hola", True, 3.5]
lista_de_listas = [[1, 2],[3, 4], [5, 6]]

# Acceder al primer valor ----- 
print(lista[0])
# al ultimo ---
print(lista[-1]) # 5

#Slicing   -- el ultimo valor no eta incluido
# [inicio, final, paso]
print(lista[1:3]) # [2,3]
print(lista[-3:-1])  # 3,4
print(lista[-3:])  #3, 4, 5
print(lista[3:]) # mostrara de 3 al ultimo
print(lista[::-1])  # [5, 4, 3, 2, 1]
print(lista) # [1, 2, 3, 4, 5]

#Añadir un elemento al final
lista.append(6)
print(lista)   # 1, 2, 3, 4, 5, 6


#Quitar el ultimo elemento
ultimo_numero = lista.pop()
print(lista)   # # 1, 2, 3, 4, 5

#Poner el elemento en una posicion cob¡ncreta
lista.insert(2, 3) # nombre.isert(posicion, valor)
print(lista)

# Eliminar un elemento por valor
print(lista_nombres)
lista_nombres.remove("Pol")
print(lista_nombres)

#Eliminar por una posicion concreta ----del[posicion]
print(lista_mixta)
del(lista_mixta[2])
print(lista_mixta)


###############################
lista_1 = [0, 1, 2]
lista_2 = [3, 4, 5]

#concatenar
lista_1.extend(lista_2)
print(lista_1)

lista_1 = lista_1 + lista_2
lista_1 += lista_2

# BUCLE 