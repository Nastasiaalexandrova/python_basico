"""
IF / ELIF / ELSE
Control de condiciones
"""

import os
os.system("cls")

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


# if not edad.isdigit():
#     print("Debes introducir el numero entero")
# elif 0 > int(edad) > 120
#     print("No me lo creo")
# else:
#     edad = int(edad)
#     diferencia = abs(mayoria edad - edad)

#     if edad < mayoria_edad:
#         print(f"Aun no puedes voter. Te faltan {mayoria_edad - edad} años")
#     else:
#         print(f"Puedes votar desde hace {diferencia} años")



# # print(edad.isdigit()) #- numero entero
# # print(edad.isdecimal()) # 
# # print(edad.isnumeric())
# # print(edad.isalpha())

# if not edad.isdigit():
#     print ("Debes introducir el numero entero")


# EJERCICIO
# pedir el numero
# pedir otro numero
# si nos son numeros le diremos que no se puede hacer - no se puede hacer la operacion y cerramos la programa
# pedir que operacion quiere: suma, resta, multiplicacion, division, exp, div_ent, Modulo
# pero si no es ninguna de estas mostraremos un error
# si divide por 0 tambien es error

# EJERCICIO
# pedir el numero
# pedir otro numero
# si nos son numeros le diremos que no se puede hacer - no se puede hacer la operacion y cerramos la programa
# pedir que operacion quiere: suma, resta, multiplicacion, division, exp, div_ent, Modulo
# pero si no es ninguna de estas mostraremos un error
# si divide por 0 tambien es error

# numero1 = input("Escribe el numero 1: ")
# numero2 = input("Escribe el numero 2: ")

# if numero1.isalpha() or numero2.isalpha():
#     print("No se puede hacer la operacion")
#     exit()

# accion = input("Que operacion quieres hacer? ").lower()
  
# if accion not in ["suma", "resta", "multiplicacion", "division", "expo", "divent", "modulo"]:
#     print("No has elegido la operacion correcta")
# elif accion == "division" and float(numero2) == 0:
#     print("No dividimos por cero")
# elif accion == "suma":
#     print(f"{numero1} + {numero2} = {float(numero1)+float(numero2)}")
# elif accion == "resta":
#     print(f"{numero1} - {numero2} = {float(numero1)-float(numero2)}")
# elif accion == "multiplicacion":
#     print(f"{numero1} * {numero2} = {float(numero1)*float(numero2)}")
# elif accion == "division":
#     print(f"{numero1} / {numero2} = {float(numero1) / float(numero2)}")
# elif accion == "divent":
#     print(f"{numero1} // {numero2} = {float(numero1) // float(numero2)}")
# elif accion == "expo":
#     print(f"{numero1} ** {numero2} = {float(numero1) ** float(numero2)}")
# elif accion == "modulo":
#     print(f"{numero1} % {numero2} = {float(numero1) % float(numero2)}")
# else:
#     pass

# num_1 = float(input("Primero numero"))
# if num_1.isalpha():
#     print("No se puede hacer")
# else:
#     print("Se puede hacer")

###################################################################################################################

#Se puede producir una excepcion a causa de lo que introduzca el usuario
# try:
#     num_1 = float(input("El numero primero:  "))
#     num_2 = float(input("El numero segundo:  "))  
    
#     operacion = input("Que operacion quieres? ")

#     if operacion == "suma":
#         print(f"{num_1} + {num_2} = {num_1 + num_2}")
#     elif operacion == "resta":
#         print(f"{num_1} - {num_2} = {num_1 - num_2}")
#     elif operacion == "multiplicacion":
#         print(f"{num_1} * {num_2} = {num_1 * num_2}")
#     elif operacion == "division":
#         print(f"{num_1} / {num_2} = {num_1 / num_2}")
#     elif operacion == "divent":
#         print(f"{num_1} // {num_2} = {num_1 // num_2}")
#     elif operacion == "expo":
#         print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
#     elif operacion == "modulo":
#         print(f"{num_1} % {num_2} = {num_1 % num_2}")
#     else:
#         print("Operación no válida.")
# except ValueError:
#     print("Debe introducir un número válido en cifras.")
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")



################################ con case

# try:
#     num_1 = float(input("El numero primero:  "))
#     num_2 = float(input("El numero segundo:  "))  
    
#     operacion = input("Que operacion quieres? ").lower()

#     match operacion:
#         case "suma":
#             print(f"{num_1} + {num_2} = {num_1 + num_2}")
#         case "resta":
#             print(f"{num_1} - {num_2} = {num_1 - num_2}")
#         case "multiplicacion":
#             print(f"{num_1} * {num_2} = {num_1 * num_2}")
#         case "division":
#             print(f"{num_1} / {num_2} = {num_1 / num_2}")
#         case "divent":
#             print(f"{num_1} // {num_2} = {num_1 // num_2}")
#         case "expo":
#             print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
#         case "modulo":
#             print(f"{num_1} % {num_2} = {num_1 % num_2}")
#         case _ :
#             print("Operación no válida.")
# except ValueError:
#     print("Debe introducir un número válido en cifras.")
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")


############################################
# try:
#     respuesta = input("Indique los numeros y la operacion a realizar\nEjemplo: 10, 5, +\n").split(", ")
#     num_1 = float(respuesta[0])
#     num_2 = float(respuesta[1])
#     operacion = respuesta[2]
   

#     match operacion:
#         case "+" | "-" | "*" | "/":
#             resultado = eval(f"{num_1} {operacion} {num_2}")
#             print(f"{num_1} {operacion} {num_2} = {resultado}")
#         case _ :
#             print("Prueba otra vez")
# except ValueError:
#     print("Introduce los numeros y symbol")
# except ZeroDivisionError:
#     print("No se puede dividir por cero")





##############otra opcion

# try:
#     respuesta = input("Indique los numeros y la operacion a realizar\nEjemplo: 10, 5, +\n").split(", ")
#     num_1 = float(respuesta[0])
#     num_2 = float(respuesta[1])
#     operacion = respuesta[2]
#     match operacion:
#         case "+":
#             resultado = num_1 + num_2
#         case "-":
#             resultado = num_1 - num_2
#         case "*":
#             resultado = num_1 * num_2
#         case "/":
#             resultado = num_1 / num_2     
#         case _ : 
#             print("Prueba otra vez")
# except ValueError:
#     print("Introduce los numeros y symbol")
# except ZeroDivisionError:
#     print("No se puede dividir por cero")
# else:
#     print(f"{num_1} {operacion} {num_2} = {resultado}")

#############################################################
frase = "Hola soy una programa de Python y estoy funccionando correctamente"
palabras_en_frase = frase.split(" ")
print(palabras_en_frase)
print(len(palabras_en_frase))
frase_2 = " ".join(palabras_en_frase)
print(frase_2)


texto_con_espacios = "     Hola que haces      "
texto_sin_espacio = texto_con_espacios.strip()
print("texto sin espacios", texto_sin_espacio)