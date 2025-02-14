# """
# ENTRADAS DEL CINE

# Vamos a crear una app para vender entradas del cine.

# Hay tres precios:
# - Entrada estándar: 9.00
# - Mayores de 65 años (seniors) : 6.90
# - Infantiles : 7.20

# Se puede vender cualquier cantidad de entradas,
# pero los menores siempre deber ir acompañados
# de un adulto.

# Al finalizar la compra mostraremos las entradas 
# y el importe total. 

# """
# # import emoji

# entradas = [9.00, 6.90, 7.20]

# while True:
#     menu = """
#     Bienvenido a nuestro cine! 🎬
#     Vamos a comprar los tickets! \U0001F600 
#     Que tipo de las entradas quieres?
#     1 - Entrada estándar: 9.00 euros
#     2 - Mayores de 65 años (seniors) : 6.90 euros
#     3 - Infantiles : 7.20 euros
#     """
#     print(menu)
#     tipo = input("Elije el numero de la opcion:   ").strip()

#     match tipo:
#         case "1":
#             try:
#                 print("\nEl precio del ticket para el adulto es 9.00 euro")
#                 cantidad = int(input("Cuantas entradas quieres?   "))
#                 if cantidad <= 0 or cantidad > 50:
#                     print("Elije la cantidad entre 1 y 50 tickets")
#                 precio = round(float(entradas[0]), 2)
#                 # precio = entradas[0]
#                 print(f"\nHas elegido {cantidad} ticket(s) para los adultos \n\nTienes que pagar: \n   {cantidad} * {precio:.2f} = {(cantidad * precio):.2f}€")
#             except ValueError:
#                 print("Ingresa el numero valido")
#         case "2":
#             print("Cada persona mayor debe estar acompañada por un adulto")
#         case "3":
#             print("Los niños deben estar acompañados por un adulto")
#         case _ :
#             print("\nElije la opcion correcta\n")




########  
# Informacion de partida
tipo_entrada = {"estandar": 9.00, "senior": 6.90, "infantil": 7.2, "dia del espectador": 5.00}

# Lo que el cliente va a comprar
lista_entradas_compradas = []

compra_activa = True

while compra_activa:

    menu = "Precios de la entradas:"
    #Leer el diccionario con los datos de la entradas
    for clave, valor in tipo_entrada.items():
        # menu += f"\n{clave.title()} : {valor:.2f}€"
        menu += f"\n{clave.title()} : {valor:.2f}€"

print(menu)