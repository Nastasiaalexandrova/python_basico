"""
IF / ELIF / ELSE
Control de condiciones
"""

# Condiciion binaria
lluve = False
if lluve:
    print("Esta lloviendo")
else: 
    print("Que sol!")

lunes = False # los lunes como pizza
jueves = True # jueves - paella
# el resto de dias un bocadillo

if lunes:
    print("Toca pizza")
elif jueves:
    print("Toca paella")
else:
    print("Toca bocadillo")

# EJERCICIO
# preguntar la edad del usuario
# si tiene menos de 12 - eres un niño/niña
# si tiene menos de 18 - eres adolescente
# si tiene menos de 30 - eres muy joven
# si tiene menos de 40 - joven, pero menos
# si tiene mas - tu puedes con todo

edad = int(input("Cuantos años tienes?"))
if edad <= 12:
    print("eres un niño/niña".capitalize())
elif edad <= 18:
    print("eres adolescente".capitalize())
elif edad <= 30:
    print("eres muy joven".capitalize())
elif edad <= 40:
    print("joven, pero menos".capitalize())
else:
    print("tu puedes con todo".capitalize())