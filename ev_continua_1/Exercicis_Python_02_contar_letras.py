"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"

Ejercicio 2b

Mostraremos el texto: "Contar palabras en un texto"
Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
. 
"""

import os
os.system("cls")

import string

# Просим пользователя ввести текст
texto = input("Por favor, introduzca un texto: ").lower()

# Создаем пустой словарь для подсчета букв
contador = {}

# Перебираем каждый символ в тексте
for caracter in texto:
    if caracter.isalpha():  # Проверяем, является ли символ буквой
        if caracter in contador:  # Если буква уже в словаре, увеличиваем счетчик
            contador[caracter] += 1
        else:
            contador[caracter] = 1  # Если буква встречается первый раз, добавляем ее в словарь

# Сортируем буквы по количеству их вхождений (по убыванию), а затем по алфавиту
letras_ordenadas = sorted(contador.items(), key=lambda x: (-x[1], x[0]))

# Выводим результат
print("El texto contiene las letras:")
for letra, cantidad in letras_ordenadas:
    if cantidad > 1:
        print(f"{letra}, {cantidad} veces")  # Если буква встречается больше 1 раза
    else:
        print(f"{letra}, 1 vez")  # Если буква встречается 1 раз
