"""
MATCH -- switch de js o java
"""

import os
os.system("cls")

# mes = "Febrero"

# match mes: 
#     case "Enero":
#         print("A NY")
#     case "Febrero":
#         print("A Canada")
#     case "March" | "Abril" | "Mayo":  # o 1ro o 2o o 3ro
#         print("A casa")
#     case _ :   ################## 
#         print("No se a donde ir")


        #############################################################+

# EJERCICIO 
# preguntar que dia de la semana es 
# si lunes - Toca sistemas
# martes, miercoles, jueves o viernes - Toca Python
# sabado o domingo - Finde 
# otra cosa - Estas confudido

attempts = 0
while attempts < 2:  # Only allow 2 attempts
    dia = input("Que dia es?   ").lower()
    match dia:
        case "lunes":
            print("Toca sistemas")
        case "martes"| "miercoles" | "jueves" | "viernes":
            print("Toca Python")
        case "sabado" | "domingo":
            print("El finde")
        case _ :
            if attempts == 0:  # First incorrect input
                print("Día no válido. Por favor, inténtalo de nuevo.")
                attempts += 1
            else:  # Second incorrect input
                print("Has cometido dos errores. Terminando el programa.")


                