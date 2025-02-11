"""
TUPLAS
es una coleccion INMUTABLE de datos
"""

mi_tupla = (3)
print(type(mi_tupla)) ########class INT
mi_tupla_2 = (3,)
print(type(mi_tupla_2)) ########class TUPLE
mi_tupla_3 = 3,4,5
print(type(mi_tupla_3))


tupla = ("Anna", "Pou", 20, "anna@email.com")
print(tupla)
# tupla[0] = "Marta" #######error
lista_temporal = list(tupla)
lista_temporal[0] = "Marta"
print(lista_temporal)
tupla = tuple(lista_temporal)
print(tupla)

print(tupla[1:3])

for item in tupla:
    print(item)

