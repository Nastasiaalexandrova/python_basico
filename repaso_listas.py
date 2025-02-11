lista_enteros = list(range(1,21,2))
print(lista_enteros)

lista_nombres = ["Pol", "Noa", "Sara", "Pepe"]   # indices 0  1  2  3

for nombre in lista_nombres:
    indice = lista_nombres.index(nombre)
    print(f"{indice}. {nombre}")

for indice, valor in enumerate(lista_nombres):
    print(f"{indice}. {valor}")


# Copia de una lista
nueva_lista_1 = lista_nombres.copy()
nueva_lista_2 = lista_nombres[:]


###############EJERCICIO
#obtener los numeros elevados al cuadrado de la serie
lista_numeros = list(range(0, 11))  # hay que obtener 0, 1, 4, 9......
lista_cuadrados = []
for i in lista_numeros:
    lista_cuadrados.append((i+1)**2)
    print(f"{i+1} {(i+1) ** 2}")
print(f"{lista_cuadrados}")
# print(f"{lista_numeros}")

###forma 22222222222222222222222222222
lista_cuadrados = print([numero**2 for numero in lista_numeros])

#necesitamos otra lista solo con los numeros elevados al cuadrado de lista_numeros 



# for index, valor in enumerate(lista_numeros):
    # lista_numeros[index] = index+100

#print(lista_numeros)

lista_ciudades = ["NY", "LA", "BCN"]
ny, la, bcn = lista_ciudades
print(bcn)