"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"

Ejercicio 2b

Mostraremos el texto: "Contar palabras en un texto"
Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
. 
"""

import os

os.system("cls")

texto = input("Por favor, introduzca un texto: ").lower() # pedimos al usuario un texto

contador = {} # creamos un diccionario para contar las letras

for caracter in texto: # miramos cada carácter del texto
    if caracter.isalpha():  # solo para letras
        if caracter in contador:
            contador[caracter] += 1  #si la letra ya está +1
        else:
            contador[caracter] = 1  # escribimos 1 para la primera vez

lista_letras = list(contador.items()) # cambio el diccionario en una lista de tuplas

def criterio_ordenacion(item): # hacemos la funccion para ordenar
    letra, cantidad = item
    return -cantidad, letra  # cantidad desc y letras hacemos asc

lista_ordenada = sorted(lista_letras, key=criterio_ordenacion) # sorteamos

print("\nEl texto contiene las letras:") # el resultado
for letra, cantidad in lista_ordenada:
    if cantidad > 1:
        print(f"{letra}, {cantidad} veces")
    else:
        print(f"{letra}, 1 vez")
