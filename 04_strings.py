"""
CADENAS DE TEXTO
"""

string_1 = 'Hola'
string_2 = "Hola"
string_3 = """Hola"""
print(string_1, string_2, string_3)

name = "Anastasiia"
surname = "Mishakova"
age = 35
phrase = "Hola. Me llamo" + " " + name + " " + surname + "." + " Yo tengo " + str(age) + " años"
print(phrase)
phrase2 = f"Hola. Me llamo {name} {surname}. Yo tengo {age} años"
print(phrase2)

# texto_final3 = "{} {}".format(texto1, texto2)
# The {} placeholders are used to indicate where you want to insert the values of texto1 and texto2.
# .format() is a method that replaces the {} placeholders with the variables provided in the format() method.
# In this case, texto1 will replace the first {}, and texto2 will replace the second {}.
# So, if texto1 = "Hello" and texto2 = "World", after running this line, texto_final3 will be "Hello World".

# nombre = input("Cual es tu nombre?")
# print(type(nombre))
# apellidos = input("Cual es tu apellidos?")
# age = input("Cual es tu edad?")
# frase3 = f"Tu nombre es {nombre} {apellidos}. Tienes {age} años"
# print(frase3)

# METODOS DE LOS STRINGS
frase = "es una frase un poco larga, pero podria serlo mas"

# Primer caracter del string
print("frase[0] -> ", frase[0])

# Ultimo caracter del string
print("frase[-1] -> ", frase[-1])

# 5 primeros caracteres
print("frase[0:6] ->", frase[0:6]) # [inicio: fin]
print("frase[:6] ->", frase[:6])

# 5 primeros caracteres
frase = "manzana"
print("frase[0:-6] ->", frase[0:-6]) # [inicio: fin]  ----m
print("frase[:-5] ->", frase[:-5])    #   ma
print("frase[-4:-2] ->", frase[-4:-2])  # ------za
print("frase[1:-6] ->", frase[1:-6])
print("frase[:] ->", frase[:]) # mostrara todo [:]

# Caracteres en posicion par
print("frase[0:6] ->", frase[::2]) # mostrara cada segundo simbolo
print("frase[0:6] ->", frase[::-1]) #invertido

# Cuantos caracteres hay en string
print("len(frase) ->", len(frase))

# Convertir el texto a mayusculas
print(frase.capitalize()) #Manzana
print(frase) # manzana
frase = frase.capitalize()
# pero tenemos que asignar para recibir Manzana   ---- frase = frase.capitalize()
print(frase.upper()) #MANZANA

# Convertir el texto a minusculas
print(frase.lower())

# Empezar el string con mayusculas - CAPITALIZE()
frase = "es una frase un poco larga, pero podria serlo mas"
frase = frase.capitalize()
print(frase)

# Invertir mayuscuklas a minusculas
print(frase.swapcase())

# Contar caracteres SENSIBLES A MINUSCULAS Y MAYUSCULAS
print("frase.count('a') ->", frase.count("a"))

print(frase.upper())

# Encontrar la posicion de un caracter o grupo de caracteres
print("frase.find('a') ->", frase.find("a"))

# Verificar si el texto se empieza por cierto caracter o grupo de caracteres
print(frase.startswith("Es")) # True
print(frase.startswith("es")) # False

# Verificar si el texto se acaba por cierto caracter o grupo de caracteres
print(frase.endswith("mas")) #True

# Verificar si el texto es convertible a numero
#print(int(frase)) ###############error
numero = "10"
print(int(numero))
print(numero.isnumeric()) #True     Solo numeros
print(numero.isalpha()) #False      Solo textos
print(numero.isalnum()) #True

# Cambiar caracteres.
print(frase.replace("a", "i"))

palabras_en_frase = frase.split(" ")
print(palabras_en_frase)
print(len(palabras_en_frase))

print(10 > 5)
print("abeja" > "flor") #False
print("abeja" < "flor") #True - a,b,c...f.... Z es la mas grande
print("abeja" < "abejb") #True

#EJERCICIO
texto = "bUeNos dIAs" #Buenos dias
texto = texto.lower().capitalize()
print(texto)