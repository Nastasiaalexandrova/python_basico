# # 62

# def sumar(*argv) :
#     print(type(argv))

# sumar(1,2)
# sumar(3,4,5)
# sumar(3,7,907)

def separarNombre(apellido_nombre: str):
    """
    Devolvera de forma separada el nombre y el apellido

    @ Params
    str -> "Apellido, Nombre"

    Return:
    tuple(str, str) -> (Nombre, Apellido)
    """
    lista = apellido_nombre.split(",")
    apellido = lista[0].strip()
    nombre = lista[1].strip()
    return nombre, apellido

nombre, apellido = separarNombre("Jobs, Steve")  # <-- Передаем ОДНУ строку
print(nombre, apellido)

# Muestra la documentación de la función correctamente
help(separarNombre)
print(separarNombre.__doc__)


# tupla = (1,2,3)
# valor1 = tupla[0] 
# valor2 = tupla[1] 
# valor3 = tupla[2] 
# print(type(tupla))
# print(type(valor1))