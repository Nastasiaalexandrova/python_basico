"""
    Mi primera programa con Python
    Variables y funcciones basicas
"""


# numero_entero = 2
# numeroEntero = 3
# print(numero_entero)

# numero1, numero2 = 2, 3
# print(numero1, numero2)

# Keep
# It
# Simple
# Stupid

numero_entero = 2
numero_decimal = 4.5

saludo = "Buenas tardes"
despedida = 'Adios'

decration = "I'm a developer"
ejemplo_comilla_triple = """
    estoy dentro de una
    comilla triple
"""

verdad = True
mentira = False

print(numero_entero)
print(type(numero_entero)) #########type
print(numero_decimal)
print(saludo)
print(ejemplo_comilla_triple)

from datetime import datetime
print(datetime.now())
########### mostrar la fecha y el tiempo

suma = 1 + 3
resta = 1 - 4
print(suma, resta)
multiplicacion = 4 * 2
division = 10 / 5 ### siempre decimales la division
#division2 = 10 / 0 ### no puedo dividir el cero
exponencial = 2 ** 3
exponencial2 = 4 ** 0.5
division_entera = 20 // 6
modulo = 20 % 3
modulo2 = 200234 % 2

suma = 4 + 8
print(suma, multiplicacion, division, exponencial, exponencial2, division_entera, modulo, modulo2)

texto1 = "buenas"
texto2 = "noches"
texto_final = texto1 + " " + texto2
print(texto_final)
print(texto1, texto2)
texto_final2 = f"{texto1} {texto2}"
print(texto_final2)
texto_final3 = "{} {}".format(texto1, texto2)
print(texto_final3)

