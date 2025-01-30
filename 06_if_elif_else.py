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

# edad = int(input("Cuantos años tienes?"))
# if edad <= 12:
#     print("eres un niño/niña".capitalize())
# elif edad <= 18:
#     print("eres adolescente".capitalize())
# elif edad <= 30:
#     print("eres muy joven".capitalize())
# elif edad <= 40:
#     print("joven, pero menos".capitalize())
# else:
#     print("tu puedes con todo".capitalize())

# # EJERCICIO
# preguntar edad
# si tiene menos de 0 o mas de 129 diremos "no lo creo"
# menos 18 - aun no puedes votar, te faltan x años
# 18 o mas - puedes votar desde hace x años

# edad = int(input("Cuantos años tienes?"))
# if edad <= 0 or edad > 129:
# # if not (1 <= edad <= 129):
# # if edad not in range(1, 130):
#     print("No me lo creo")
# elif edad < 18:
#     print("Aun no puedes votar. Te faltan " + str(18 - edad) + " años")
# else:
#     print(f"Puedes votar desde hace {edad - 18} años")

# EJERCICIO
# pedir el numero
# pedir otro numero
# si nos son numeros le diremos que no se puede hacer - no se puede hacer la operacion y cerramos la programa
# pedir que operacion quiere: suma, resta, multiplicacion, division, exp, div_ent, Modulo
# pero si no es ninguna de estas mostraremos un error
# si divide por 0 tambien es error

numero1 = input("Escribe el numero 1: ")
numero2 = input("Escribe el numero 2: ")
accion = input("Que operacion quieres hacer? ").lower()

if numero1.isnumeric() == False and numero2.isnumeric() == False:
    print("No se puede hacer la operacion")
elif accion not in ["suma", "resta", "multiplicacion", "division"]:
    print("No has elegido la operacion correcta")
elif accion == "division" and int(numero2) == 0:
    print("No dividimos por cero")
elif accion == "suma":
    print(f"{numero1} + {numero2} = {int(numero1)+int(numero2)}")
elif accion == "resta":
    print(f"{numero1} - {numero2} = {int(numero1)-int(numero2)}")
elif accion == "multiplicacion":
    print(f"{numero1} * {numero2} = {int(numero1)*int(numero2)}")
elif accion == "division":
    print(f"{numero1} / {numero2} = {int(numero1) / int(numero2)}")
else:
    pass