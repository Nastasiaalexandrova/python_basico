

inventario = {"manzanas": 10, "peras": 15, "kiwis": 5, "limones": 4, "naranjas": 7, "melones": "viernes"}

inventario["piñas"] = 3
inventario["tomates"] = 5


#modificar la cantidad con una nueva
inventario["naranjas"] = 4

#incrementar
inventario["kiwis"] += 5

print(inventario)

# inventario.popitem quita el ultimo

fruta = inventario.pop("peras") #pop("clave")
print(inventario) #{'manzanas': 10, 'peras': 15, 'kiwis': 10, 'limones': 4, 'naranjas': 4, 'melones': 'viernes', 'piñas': 3, 'tomates': 5}
print(fruta) #{'manzanas': 10, 'kiwis': 10, 'limones': 4, 'naranjas': 4, 'melones': 'viernes', 'piñas': 3, 'tomates': 5}

inventario.popitem()
print(inventario) # {'manzanas': 10, 'kiwis': 10, 'limones': 4, 'naranjas': 4, 'melones': 'viernes', 'piñas': 3}

# salida ordenada
for producto in sorted(inventario): # sorta solo para ahora
    print(f"producto: {producto}")

# salida reversed
for producto in sorted(inventario, reverse = True):  # 
    print(f"producto: {producto}")

