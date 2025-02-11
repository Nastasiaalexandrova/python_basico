"""
EJERCICIO
tenemos un sitio que registra los accesos de los usuarios

necesitamos un mmenu con estas opciones
-añadiremos un usuario(si no existe ya)
-añadiremos auna visita al usuario indicado (si el usuario no existe mostrar un error)
-mostraremos las visitas del usuario que se decida (si el usuario no existe mostrar un error)
-mostraremos las visitas de todos los usuarios (si no hay usuarios todavia indicarlo)
x Salir

hay que hacerlo con diccionarios
-"""

# usuarios = {"usuario":"", "entradas":""}
# # usuarios["usuario"] = input("Escribe tu nombre:   ")
# usuarios["entradas"] = 0

# while True:
#     print("\nMenu de opciones:")
#     print("1. Añadir usuario")
#     print("2. Añadir visita a un usuario")
#     print("3. Mostrar visitas de un usuario")
#     print("4. Mostrar visitas de todos los usuarios")
#     print("5. Salir")

#     opcion = input("Selecciona la opcion:   ")

#     if opcion == "1":
#         nombre = input(print("Escribe el nombre:   "))
#         if nombre in usuarios["usuario"]:
#             print(f"El usuario {nombre} ya existe")
#         else:
#             usuario_nuevo = {"usuario":"{nombre}", "entradas":"0"}
#             usuarios.update(usuario_nuevo)
#             print(f"El usuario {usuario_nuevo} añadido")


# for usuario, entradas in usuarios.items():
#     if usuario in usuarios == "":
#         print("No hay usuarios")
#     else:
#         usuarios_lista = usuarios.update("usuario")
#         usuarios["entradas"] = 1                                     




    # print(f"{usuario} con {entradas} entradas")
    
# import os
# os.system("cls")

# users = {} 

# while True:
#     menu = """
#     1. Añadir usuario
#     2. Añadir visita a un usuario
#     3. Mostrar visitas de un usuario
#     4. Mostrar visitas de todos los usuarios
#     5. Salir
# """
    # print(menu)

    # opcion = input("Elige tu opcion:    ").strip().lower()

    # match opcion:
    #     case "1":
    #         # nombre = " "
    #         new_user = input("Escribe el nombre:   ").strip().title()
    #         if new_user not in usuarios:
    #             usuarios[new_user] = {"entradas": 0 } # Si no existe, añadir el usuario con 0 visitas
    #             print(f"El usuario {new_user} añadido")
    #         else:
    #             print("El usuario ya existe")
    #     case "2":
    #         nombre = input("Introduce el nombre del usuario al que quieres añadir una visita: ").strip()
    #         if nombre in usuarios:
    #             usuarios[nombre]["entradas"] += 1
    #             print(f"La visita del usuario {nombre} añadida")
    #     case "3":
    #         nombre = input("Las entradas de que usuario quieres ver?   ")
    #         # if nombre in usuarios:
    #         pass
    #     case "4":
    #         pass
    #     case "x":
    #         print("Fin del programa")
    #         break
    #     case _ :
    #         print("Opcion no es reconocida. \nVuelvelo a probar")



import os
os.system("cls")

# Dictionary to store users and their visits
users = []

while True:
    menu = """
    1. Añadir usuario
    2. Añadir visita a un usuario
    3. Mostrar visitas de un usuario
    4. Mostrar visitas de todos los usuarios
    5. Salir
    """
    print(menu)
    opcion = input("Elige tu opcion --> ").strip().lower()

    match opcion:
        case "1":
            # Add a new user
            new_user = input("Nuevo usuario --> ").strip().title()
            # Check if the user already exists
            user_exists = False
            for user in users:
                if user["nombre"] == new_user:
                    print("El usuario ya existe.")
                    user_exists = True
                    break
            if not user_exists:
                user_dic = {"nombre": new_user, "visitas": 0}
                users.append(user_dic)  # Add new user to the list
                print(f"El usuario {new_user} añadido.")

        case "2":
            # Add a visit to an existing user
            user_name = input("Introduce el nombre del usuario al que quieres añadir una visita: ").strip().title()
            user_found = False
            for user in users:
                if user["nombre"] == user_name:
                    user["visitas"] += 1  # Increment the visit count
                    print(f"Visita añadida al usuario {user_name}.")
                    user_found = True
                    break
            if not user_found:
                print(f"El usuario {user_name} no existe.")

        case "3":
            # Show visits of a specific user
            user_name = input("Las entradas de que usuario quieres ver?   ").strip().title()
            user_found = False
            for user in users:
                if user["nombre"] == user_name:
                    print(f"El usuario {user_name} tiene {user['visitas']} visitas.")
                    user_found = True
                    break
            if not user_found:
                print(f"El usuario {user_name} no existe.")

        case "4":
            # Show visits of all users
            if users:
                for user in users:
                    print(f"{user['nombre']} tiene {user['visitas']} visitas.")
            else:
                print("No hay usuarios todavía.")

        case "5":
            # Exit the program
            print("Fin del programa")
            break

        case _:
            # Invalid option
            print("Opción no reconocida.\nVuélvelo a probar.")