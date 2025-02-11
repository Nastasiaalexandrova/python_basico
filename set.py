"""
SET   conjunto logico
Los SETs no pueden tener valores repetidos
"""


lista_numeros = [1, 2, 2, 5, 7, 5, 4, 1]
print(lista_numeros)
lista_sin_repeticiones = list(set(lista_numeros))
print(lista_sin_repeticiones) # en [] -- lista
lista_sin_repeticiones_2 = set(lista_numeros)
print(lista_sin_repeticiones_2)  # en {} --- set

