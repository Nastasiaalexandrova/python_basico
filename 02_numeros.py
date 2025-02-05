"""
PROPIEDADES DE LO NUMEROS
"""
import os
os.system("cls")

suma = 1 + 3
resta = 1 - 4
#print(suma, resta)
multiplicacion = 4 * 2
division = 10 / 5 ### siempre decimales la division
#division2 = 10 / 0 ### no puedo dividir el cero
exponencial = 2 ** 3
exponencial2 = 4 ** 0.5
division_entera = 20 // 6
modulo = 20 % 3
print(f"MODULOOOOOOOOOOOOOOOOOOOO 20%3 {modulo}")
modulo2 = 200234 % 2

operacion = (1 + 2) - (3 * 30 / 5) # -15.0
# operacion = (1 + 2) - (3 * (30 / 5)) # -15.0
print(operacion)

# OPERACIONES DE COMPARACION
# si son iguales o distintos
comparacion_1 = 1 == 2
print(comparacion_1) # False
comparacion_2 = 1 != 2
print(comparacion_2) # True

#si un numero es mayor o menor
print(1 > 2) #False
print(1 > 1) #False
print(1 >= 1) #True


verdadero = True
# True = False # Error critico
print( verdadero )
print("!True")

edad = input("Escribe")
print(edad.isdigit()) #- numero entero
print(edad.isdecimal()) # 
print(edad.isnumeric())

# METODOS PARA NUMEROS
# redondear el numero a la izquierda o a la derecha
redondear_izquierda = round