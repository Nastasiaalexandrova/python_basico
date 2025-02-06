"""
El usuario introduce un número entero, como máximo 100
ese número es el límite
Desde 0 hasta el número introducido (los dos incluidos), vamos a listar todos los números
Pero...
-- Si el número es multiplo de 3, escribiremos 3 - FIZZ
-- Si el número es multiplo de 5, escribiremos 3 - BUZZ
-- Si el número es multiplo de 3 y de 5, escribiremos 3 - FIZZ-BUZZ
-- En los demás casos sólo el número
-- Si el usuario escribe más de 100 o menos de 0, diremos "El número es incorrecto"
"""


import os
os.system("cls")

# try:
#     numero = int(input("Introduce el numero de 0 a 100:   "))

#     if int(numero) < 0 or int(numero) > 100:
#         print("El número es incorrecto")
#     elif int(numero) == 0:
#         print("Numero es ", numero)
#     elif int(numero) % 15 == 0:
#         print("FIZZ-BUZZ")
#     elif int(numero) % 3 == 0:
#         print("FIZZ")
#     elif int(numero) % 5 == 0:
#         print("BUZZ")
#     else:
#         print("Numero es ", numero)
# except ValueError:
#     print("Introduce el numero entero valido")
    

try:
    referencia = int(input("El numero:       "))
    if referencia < 0 or referencia > 100:
        print("Incorrecto")
        exit()
    if 0 <= referencia <= 100:
        for num in range(0, referencia+1, 1):
            if num == 0:
                print(0)
            elif num % 3 == 0 and num % 5 == 0:
                print(f"{num} FIZZ-BUZZ")
            elif num % 3 == 0:
                print(f"{num} FIZZ")
            elif num % 5 == 0:
                print(f"{num} BUZZ")
            else:
                print(f"{num}")
except:
    print("print el numero entero")




##################22222222222222222222      Using a Dictionary for Mapping Conditions
# numero = int(input("Introduce el numero de 0 a 100:   "))

# if numero < 0 or numero > 100:
#     print("Check your number again")
# else:
#     output = ""
#     if numero % 3 == 0:
#         output += "FIZZ"
#     if numero % 5 == 0:
#         output += "BUZZ"
    
#     # If nothing was added to output, just print the number
#     print(output if output else numero)


##############3333333333333333333333 Using a Function for Reusability
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FIZZ-BUZZ"
#     elif number % 3 == 0:
#         return "FIZZ"
#     elif number % 5 == 0:
#         return "BUZZ"
#     else:
#         return number

# numero = int(input("Introduce el numero de 0 a 100:   "))

# if numero < 0 or numero > 100:
#     print("Check your number again")
# else:
#     print(fizz_buzz(numero))


##########################444444444444444       Using a Ternary Conditional (Inline)
# numero = int(input("Introduce el numero de 0 a 100:   "))

# if numero < 0 or numero > 100:
#     print("Check your number again")
# else:
#     print("FIZZ-BUZZ" if numero % 15 == 0 else "FIZZ" if numero % 3 == 0 else "BUZZ" if numero % 5 == 0 else numero)



##########################555555555555555555555     Using List Comprehension or String Concatenation
# numero = int(input("Introduce el numero de 0 a 100:   "))

# if numero < 0 or numero > 100:
#     print("Check your number again")
# else:
#     result = ''.join([ "FIZZ" if numero % 3 == 0 else "", "BUZZ" if numero % 5 == 0 else "" ])
#     print(result if result else numero)



#############666666666666666666    Using a Class (for a more object-oriented approach)
# class FizzBuzz:
#     def __init__(self, number):
#         self.number = number

#     def get_result(self):
#         if self.number % 15 == 0:
#             return "FIZZ-BUZZ"
#         elif self.number % 3 == 0:
#             return "FIZZ"
#         elif self.number % 5 == 0:
#             return "BUZZ"
#         else:
#             return self.number

# numero = int(input("Introduce el numero de 0 a 100:   "))

# if numero < 0 or numero > 100:
#     print("Check your number again")
# else:
#     fb = FizzBuzz(numero)
#     print(fb.get_result())
