
hay_animal = False
try:
    animales = ["gato", "perro", "caballo", "paloma", "murcielago", "leon", "mono"]
    letra = input("Introduce la letra:    ")
    if letra.isalpha():
        for animal in animales:
            if animal.startswith(letra):
                print(f"Tu animal es: {animal}")
                hay_animal = True
    if not hay_animal:
        print(f"No hay los animales en la lista que se empiezan de {letra}")
        
except ValueError:
    print("Introduce la letra sin simbolos")

# animales = ["gato", "perro", "caballo", "paloma", "murcielago", "leon", "mono"]
#     letra = input("Introduce la letra:    ")
#     if letra.isalpha():
#         for animal in animales:
#             if letra == []