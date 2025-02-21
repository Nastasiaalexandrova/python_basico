"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 1

Un número primo es aquel que sólo es divisible por sí mismo o uno.

Pediremos al usuario un número entero.
Si escribe algo que no sea un número entero la aplicación debe responder: 
    "Has de introducir un número entero".
Daremos hasta tres oportunidades para que nos facilite un dato correcto.
Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
la aplicación finalizará mostrando este mensaje:
    "No has podido introducir un número entero en tres oportunidades
    Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
    ".
Si escribe un número entero puede pasar que
-- sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X es primo".
-- no sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X no es primo".

. 
"""
import os
os.system("cls")


intentos = 3  # establecemos los intentos
while intentos > 0:
    try:
        numero = int(input("Escribe el numero entero:    "))
        if numero <= 1:   # si el numero es menos o igual que 1 - no es el primo
            print(f"El numero {numero} no es primo")
        else:
            es_primo = True   #añadimos la logica si es primo
            for i in range (2, numero):   #a partir del numero dos comprobamos si el numero es primo
                if numero % i == 0:   #si el numero se puede dividir en otro aparte del 1 y al mismo numero - eso significa que no es primo
                    es_primo = False
                    break
            if es_primo:
                print(f"El numero {numero} es primo")
            else:
                print(f"El numero {numero} no es primo")
        break

    except ValueError:   # contamos la cantidad de los intentos dejados
        intentos -= 1
        print(f"No has introducido un número entero. Te quedan {intentos} intentos.")
        if intentos == 0:
            print("No has podido introducir un número entero en tres oportunidades \n Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación")
