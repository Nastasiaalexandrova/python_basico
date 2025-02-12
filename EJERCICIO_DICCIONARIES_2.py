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
    opcion = input("Enter the option:   ").strip().lower()
    match opcion:
        case "1":
            new_user = input("Add the name of a new user:   ")
            user_exists = False
            for user in users:
                if new_user == user["name"]:
                    user_exists = True
                    print("The user already exists")
                    break
            if not user_exists:
                user_dic = {"name": new_user, "visits": 0}
                users.append(user_dic)
                print(f"The user {new_user} was added")
        case "2":
            user_name = input("Enter the user name")
            
            if user("visits") in users == 0:
                user("visits") += 1
                print(f"The user {user("name")} tiene {user("visits")} visits")
                
