"""
BOOLEANS
"""

verdadero = True
falso = False
Verdadero = True
autentico = True
print(id(verdadero)) #  140722683412912
print(id(Verdadero)) #  140722683412912

#Algunos valores tienen asignado False
# 0 -> el numero 0
# "" -- string vacio
# [] -- lista vacia

print(verdadero == autentico)
print()

print(bool(0))

if 0:
    print("el 0 es verdadero")
else:
    print("El cero es falso")


