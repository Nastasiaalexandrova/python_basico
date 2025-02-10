"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 1

Un número primo es aquel que sólo es divisible por sí mismo o uno.

Pediremos al usuario un número entero.
Si escribe algo que no sea un número entero la aplicación debe responder: 
    "Has de introducir un número entero".
Daremos hasta tres oportunidades para que nos facilite un dato correcto.
Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
la aplicación finalizará mostrando este mensaje:
    "No has podido introducir un número entero en tres oportunidades
    Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
    ".
Si escribe un número entero puede pasar que
-- sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X es primo".
-- no sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X no es primo".

. 
"""
import os
os.system("cls")

# numero = input("Escribe un numero entero______")
# intentos = 3

# while intentos > 0:
#     if numero % 1 == numero:
#         print(f"El numero {numero} es primo")
#     elif numero == float(numero):
#         print("Has de introducir un número entero")
#     else:
#         print("No has podido introducir un número entero en tres oportunidades. \n Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.")




# Количество попыток, которое даем пользователю для ввода правильного числа
# intentos = 3

# # Цикл будет выполняться до тех пор, пока у пользователя есть попытки
# while intentos > 0:
#     try:
#         # Пытаемся получить целое число от пользователя
#         numero = int(input("Escribe un número entero: "))  # Вводим число и пытаемся преобразовать в целое

#         # Проверяем, является ли число простым
#         if numero <= 1:
#             # Числа 1 и меньше не могут быть простыми
#             print(f"El número {numero} no es primo")  # Сообщаем, что число не простое
#         else:
#             # Флаг, который определяет, является ли число простым
#             es_primo = True  # Предполагаем, что число простое

#             # Проверка на делимость числа от 2 до самого числа - 1
#             for i in range(2, numero):  # Перебираем числа от 2 до числа-1
#                 if numero % i == 0:  # Если число делится на i без остатка
#                     es_primo = False  # Значит, это не простое число
#                     break  # Останавливаем цикл, так как нашли делитель

#             # Выводим результат: если флаг es_primo остался True, то число простое
#             if es_primo:
#                 print(f"El número {numero} es primo")  # Число простое
#             else:
#                 print(f"El número {numero} no es primo")  # Число не простое
        
#         # Прерываем цикл после успешного ввода и выполнения всех проверок
#         break

#     except ValueError:
#         # Если ввод не является целым числом, возникнет исключение ValueError
#         intentos -= 1  # Уменьшаем количество попыток
#         if intentos > 0:
#             # Если у нас еще есть попытки, выводим сообщение о необходимости ввести число
#             print("Has de introducir un número entero. Te quedan", intentos, "intentos.")
#         else:
#             # Если попытки закончились, выводим финальное сообщение
#             print("No has podido introducir un número entero en tres oportunidades. Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.")

intentos = 3  # establecemos los intentos
while intentos > 0:
    try:
        numero = int(input("Escribe el numero entero:    "))
        if numero <= 1:   # si el numero es menos o igual que 1 - no es el primo
            print(f"El numero {numero} no es primo")
        else:
            es_primo = True   #añadimos la logica si es primo
            for i in range (2, numero):   #a partir del numero dos comprobamos si el numero es primo
                if numero % i == 0:   #si el numero se puede dividir en otro aparte del 1 y al mismo numero - eso significa que no es primo
                    es_primo = False
                    break
            if es_primo:
                print(f"El numero {numero} es primo")
            else:
                print(f"El numero {numero} no es primo")
        break

    except ValueError:   # contamos la cantidad de los intentos dejados
        intentos -= 1
        print(f"No has introducido un número entero. Te quedan {intentos} intentos.")
        if intentos == 0:
            print("No has podido introducir un número entero en tres oportunidades \n Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación")
