"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""

import os
os.system("cls")

print("Conversor de segundos")
segundos = input("Indice la cantidad del segundos:___") 

if not segundos.isdigit():   # comprobamos si el numero es el numero
    print("Intenta de nuevo")
else:
    segundos = int(segundos)   # segundos usamos como el numero entero
    if segundos < 60:
        print(f"{segundos} segundos es menos que 1 minuto")
    elif segundos >= 60 and segundos < 3600:    # 3600segundos = 60 minutos, no incluimos 60 minutos porque eso es una hora ya
        minutos = segundos // 60  #comprobaremos cuantos minutos enteros contiene esta cantidad de segundos
        segundos_resto_minutos = segundos % 60   # contamos el resto de segundos
        print(f"{segundos} segundos son {minutos} minutos and {segundos_resto_minutos} segundos") # y mostramos el resultado
    elif segundos >= 3600 and segundos < 86400:  # 86400 es un dia --- pues miremos cuantas horas y no incluimos 24 horas porque eso es el 
        #########  abajo tiene al misma logica del codigo
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos_resto_horas = segundos % 60
        print(f"{segundos} segundos son {int(horas)} horas {int(minutos)} minutos and {segundos_resto_horas} segundos")
    elif segundos >= 86400 and segundos < 604800:
        dias = segundos // 86400
        horas = (segundos % 86400) // 3600
        minutos = (segundos % 3600) // 60
        segundos_resto_dias = segundos % 60
        print(f"{segundos} son {dias} dias {horas} horas {minutos} minutos {segundos_resto_dias} segundos")
    elif segundos >= 604800:
        semanas = segundos // 604800
        dias = (segundos % 604800) // 86400
        horas = (segundos % 86400) // 3600
        minutos = (segundos % 3600) // 60
        segundos_resto_semanas = segundos % 60
        print(f"{segundos} son {semanas} semanas {dias} dias {horas} horas {minutos} minutos {segundos_resto_semanas} segundos")
