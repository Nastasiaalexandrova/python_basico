"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 3
Un anagrama es un texto o palabra resultante de modificar el orden de otro texto o palabra.
Los textos deberán ir sin tildes (acentos o diéresis)
No se tienen en cuenta mayúsculas ni espacios.

Mostraremos el mensaje: "Anagramas"
Pediremos al usuario un texto/palabra.
Pediremos al usuario un segundo texto/palabra
Responderemos si ambos son anagramas o no.

Por ejemplo:
    "Introduzca el primer texto --> " Pedro
    "Introduzca el segundo texto --> " Poder
    "Son anagramas --> Sí"

Otro ejemplo:
    "Introduzca el primer texto --> " Ramon
    "Introduzca el segundo texto --> " Morir
    "Son anagramas --> No"
 
"""
import os
os.system("cls")

print("Anagramas")
primero = input("Escribe el primero texto____").lower().strip()   #borramos los espacios y cambiamos todas las letras en minusculas para comparar las palabras
segundo = input("Escribe el segundo texto____").lower().strip()
if not primero.isalpha() or not segundo.isalpha():   # comprobamos si las palabras consisten de las letras 
    print("Intentalo de nuevo sin numeros and otros simbolos")
else: 
    if len(primero.strip()) != len(segundo.strip()):   # comprobamos la longtitud de las palabras
        print("Son anagramas --> No")
    else:
        letras_1 = sorted(primero)   # hacemos la clasificacion de las letras
        letras_2 = sorted(segundo)   
        if letras_1 == letras_2:   # comparamos
            print("Son anagramas --> Si")
        else:
            print("Son anagramas --> No")
