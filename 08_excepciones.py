"""
EXCEPCIONES
Son errores que se producen durante la ejecutacion del programa
y lo interrumpen
"""

import os
os.system("cls")

#try / except
#si hay try debe 

num = float(input("Escribe el numero.... "))

try: #intentamos ejecutar el codigo
    num = float(input("Escribe el numero.... "))
    #print( 1 / 0 )
    # print("Despues de la division por cero")
except ValueError: #Error de conversion de tipos
    print("Has introducir el numero en cifras")
except ZeroDivisionError:
    print("No se puede dividir por cero") # Error po division por cero
    # Si se produce una excepcion, ejectamos este otro codigo
except:
    #Si se puede una excepcion, ejecutamos este otro codigo
    print("Ha ocurrido un error") #Error genercio

print("El programa continua....")

# try: 
#     # Intenta hacer algo
#     pass
# except:
#     # Si falta ejecuta esto 
#     pass
# else:
#     # Si no falta ejecuta esto 
#     pass
# finally:
#     # Se ejecuta siempre
#     pass
# print("Aqui habra mas codigo")
