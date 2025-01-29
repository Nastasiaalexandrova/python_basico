"""
CARACTERISTICAS BASICAS DE PYTHON
"""

# VARIABLES
# Una variable es un espacio de memoria para guardar datos
# por tanto es un contenedor

# PARA CREAR UNA VARIABLE...
# identificador = valor

# Hay reglas para llamar a los identificadores = nombre de variable
# No se puede hacer:
#     1variable con numeros
#     $variable con simbolos especiales
# De estos errores nos avisara VSC

# No debemos hacer(no son exactamente errores):
#     Contener caracteres fuera del ingles
#     Empezar por guion bajo (reservado para determinados situaciones)

# Que debemos hacer:
#     Nombrar nuestars variables con palabras descriptivas
#     Podemos usar mas de una palabra separada por un guion bajo(PEP-8)
#     Intentar que las lineas del codigo no sean muy largas
#     Utilizar palabras rezervadas - True, False etc.......

# Las variables tienen tipo 
#     numeros -> int, float and complejos
#     texto -> str
#     booleanos -> True / False


En Python NO existen los constantes
PI = 3.1416


# Python es de tipado dinamico  &&&& de tipado fuerte

numero = 4
numero = "uno"
suma = numero + 2  #ERROR -> no se pueden sumar numeros y texto
concatenacion = numero + str(2)
# suma_numerica = "1" + 2 # error
suma_numerica = int("1") + 2 
print(suma_numerica)
