"""
for
"""

import os
os.system("cls")

nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]
edades = [25, 30, 35, 40, 45, 28, 24, 75, 89, 234]

# para cada nombre en nombres
# for nombre in nombres:
#     print(nombre)

# for edad in edades:
#     print(edad)

# print(nombre)  # #mostrara el ultimo elemento
# print(edad)


# To choose the names that starts from "P"
# for nombre in nombres:
#     if nombre.lower().startswith("P"):
#         print(nombre)

# for edad in edades:
#     if edad.startswith("2"):
#         print(edad)   #AttributeError: 'int' object has no attribute 'startswith'

#Mostrar los nombres que empiezan por "P"
check = "P"
#Crear el bucle para acceder a cada elemento de  la lista
### 11111111
for nombre in nombres:
    # if nombre[0].lower() == check.lower():
    #     print(nombre)
### 22222
    if nombre.lower().startswith(check.lower()):
        print(nombre.capitalize())

######Ejercicio mostrar los numeros que empiezan por 2
# for edad in edades:
#     edad = str(edad)
#     if edad.startswith("3"):
#         print(edad)    ###########correct

for edad in edades:
    if str(edad)[0] == "2":
        print(f"{edad} + {edad} = {edad + edad}")

#SUMA DE LOS NUMEROS QUE SE EMPIEZAN POR "2"
# check = 2
# suma = 0



# for edad in edades:
#     if str(edad).startswith(str(check)):
#         print(edad, end=" ")
#         suma += edad
# print(end="\n")
# print("\nSuma es", suma, end = " ")
# # print("/nLa suma de los numeros que se empiezan por "2" es {suma}")


######mostrar el medio
suma = 0
cantidad = len(edades)
for edad in edades:
    edad = int(edad)
    suma += edad
print(f"La suma TOTAL es: {suma}")
print(f"Hay {cantidad} elementos")
print(f"El medio es: {suma} / {cantidad} = {suma / cantidad}")


################# Check Luis en la lista
nombre_a_buscar = "Luis"
# nombre_a_buscar = "Alba"
# "Luis esta en la lista"   "Alba o esta en la lista"

for nombre in nombres:
    print(nombre)
    if nombre_a_buscar.lower() == nombre.lower():
        print(f"{nombre_a_buscar} esta en la lista")
        break
else:
    print(f"{nombre_a_buscar} no esta en la lista")

##############Que nombres de la lista contienen la letra "o"
nombres_con_o = []
for nombre in nombres:
    indice = nombres.index(nombre) + 1
    if "o" in nombre.lower():
        print(f"{indice}. {nombre}")
        nombres_con_o.append(nombre)
        print(nombres_con_o)
    else:
        print('No hay nombres con "o"')

print(list(range(10)))
print(range(10))
for num in range(10):
    # print(num+1)
    print(num)

# for(let i=0; i<nombres.length, i++)
for  index in range(len(nombres)):
    print(f"{index+1} {nombres[index]}")