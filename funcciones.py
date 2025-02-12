"""
 FUNCCIONES
"""

#declaracion
def sumar() :
    print(1 + 2)

#invocacion
sumar()

#declaracion2
def sumar() :
    return 1 + 2
print(sumar())

#declaracion3
def sumar(num1, num2):
    return num1 + num2

print(sumar(11, 7))
print(sumar(11.3, 7.6))
print(sumar("hola ", "adios"))

######### LO QUE HAY EN LOS PARENTENSIS SON PARAMETROS
#########   eN LA EJECUICION / INOVACION LO QUE HAY EN LOS PARENTENSIS SON LOS ARGUMENTOS

resultado = sumar(2, 3)


#EJEMPLO DE FUNCCIONES:
# para ver si el numero es primo
# para corregir los nombres mal escritos
# para calcular algo



# def prueba_variable():
#     variable = "Soy una prueba"
# if True:
#     variable = "Soy una prueba"
# print(variable)


variable2 = "Otra cosa"
def prueba_variable():
    variable2 = "Soy una prueba"
print(variable2)



# def add_user (new_user, users) :
#      user_dic = {"nombre": new_user, "visitas": 0}
#     users.append(user_dic)  # Add new user to the list
#     return f"El usuario {new_user} ha sido añadido."

def mostrar_datos_alumno(nombre, apellido, becado = False):
    if becado:
        becado = "Si"
    else:
        becado = "No"
    return f"El alumno {nombre} {apellido} tiene beca? -----{becado}"  

alumno_1 = mostrar_datos_alumno("Anna", "Garcia", False)
print(alumno_1)
alumno_2 = mostrar_datos_alumno("Joan", "Pou", True)
print(alumno_2)


def sumar(*argv): #argumento variable
    print(argv)
    print(type(argv))
    suma = 0
    for i in argv:
        suma += i
    print(f"La suma es {suma}")
sumar(1, 2)
sumar(3, 4, 5)
sumar(3, 7, 907)

# def sumar2(num_3):
    # num_1 = input("primero ")
    # num_2 = input("segundo ")
#     num_3 = num_1 + num_2

# sumar2(num_3)

