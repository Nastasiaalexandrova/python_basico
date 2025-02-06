"""
Recibimos el texto
Con este texto vamos a generar otro sin las vocales ni los espacios
"""
import os
os.system("cls")


# try:
#     texto = str(input("Introduce el texto     "))
#     letras = "a", "u", "e", "o", "i", "y", " "
#     texto_modificado = ""
#     for i in texto:
#         if i not in letras:
#             texto_modificado += i
#         print(f"{texto_modificado}")

# except:
#     print("Try again")

###########2222222222222222222222
texto = str(input("Introduce el texto     "))

exclusiones = "aeiou y"
ex_total = exclusiones + exclusiones.upper()
# exclusiones =  ["a", "u", "e", "o", "i", "y", " "]


for caracter in ex_total:
    texto = texto.replace(caracter, "")

print(texto)

#################################################################
"""
Vamos pedir el numero entero
"""
try:
    num = int(input("Introduce el numero"))
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i} ")
except ValueError:
    print("Introduce el numero!!!!!!!!!")
