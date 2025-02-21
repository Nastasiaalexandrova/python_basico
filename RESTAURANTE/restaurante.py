"""
Vamos a gestionar restaurantes

Cada uno tiene:
-- nombre
-- especialidad
-- turnos 
        -pueder haber como maximo 3 clientes
        -si se realiza la reserva diremos "Rezerva realizada a [nombre_cliente]"
        -y si no - "no se ha podido realizar la rezerva. Pruebe en otro turno"
-- clientes

Del cliente vamos a necesitar (de momento)
solo el nombre

Ejemplo de uso:
cliente_1 = Cliente("Anna")
restaurante_1 = Restaurante("Can Pizza", "Italiana", [13, 14, 15, 20, 21, 22])

"""
import os
os.system("cls")

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Restaurante:
    def __init__(self, nombre, especialidad, turnos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = {turno: [] for turno in turnos}  # Diccionario para almacenar las reservas de cada turno
    
    def reservar(self, turno, cliente):
        if turno not in self.turnos:
            print(f"El turno {turno} no está disponible en {self.nombre}.")
            return False
        
        if len(self.turnos[turno]) < 3:  # Comprobar si el turno tiene menos de 3 clientes
            self.turnos[turno].append(cliente.nombre)  # Añadir el nombre del cliente a la lista de ese turno
            print(f"Reserva realizada a {cliente.nombre} en {self.nombre} a las {turno}.")
            return True
        else:
            print(f"No se ha podido realizar la reserva para {cliente.nombre}. Pruebe en otro turno.")
            return False

restaurante_1 = Restaurante("Can Pizza", "Italiana", [13, 14, 15, 20, 21, 22])
restaurante_2 = Restaurante("Don Chingon", "Mexicana", [13, 14, 15, 20, 21, 22])
restaurante_3 = Restaurante("El Pueblo Libre", "Peruana", [13, 14, 15, 20, 21, 22])
restaurante_4 = Restaurante("3 Focs", "Catalana", [13, 14, 15, 20, 21, 22])

saludo = print("\n\n\nHola! Bienvenido al servicio de reservas!\n")
while True:
    menu = """
    Hoy puedes disfrutar los siguientes:
    1. "Can Pizza" con la cocina Italiana
    2. "Don Chingon" con la cocina Mexicana
    3. "El Pueblo Libre" con la cocina Peruana
    4. "3 Focs" con la cocina Catalana
    """
    print(menu)
    
    # Elección del restaurante por el usuario
    restaurante_eleccion = input("Elige el restaurante (1, 2, 3, 4) para hacer la reserva -->  ")
    
    if restaurante_eleccion == '1':
        restaurante = restaurante_1
    elif restaurante_eleccion == '2':
        restaurante = restaurante_2
    elif restaurante_eleccion == '3':
        restaurante = restaurante_3
    elif restaurante_eleccion == '4':
        restaurante = restaurante_4
    else:
        print("Opción inválida. Por favor, elige un número entre 1 y 4.")
        continue
    
    # Pedir el nombre del cliente
    cliente_nombre = input("Introduce tu nombre: ")
    cliente = Cliente(cliente_nombre)
    
    # Pedir el turno de la reserva
    turno = int(input(f"Elige el turno (de los disponibles: {restaurante.turnos.keys()}): "))
    
    # Intentar hacer la reserva
    restaurante.reservar(turno, cliente)
    
    # Preguntar si quiere hacer otra reserva
    otra_reserva = input("¿Quieres hacer otra reserva? (sí/no): ")
    if otra_reserva.lower() != 'sí':
        print("¡Gracias por usar nuestro servicio de reservas!")
        break



# class Cliente:
#     def __init__(self, nombre):
#         self.nombre = nombre
# class Restaurante:
#         def __init__(self, nombre, especialidad, turnos):
#             self.nombre = nombre
#             self.especialidad = especialidad
#             self.turnos = {turno: [] for turno in turnos}

# saludo = print("Hola! Bienvenido al servicio de rezervas!")
# print(saludo)
# while True:

#     menu= """
#     Hoy puedes disfrutar los siguientes:
#     1. "Can Pizza" con la cocina Italiana
#     2. "Don Chingon" con la cocina Mexicana
#     3. "El Pueblo Libre" con la cocina Peruana
#     4. "3 Focs" con la cocina Catalana
#     """
#     print(menu)

    
            
#     restaurante = input("Elige el restaurante -->  ")

#     restaurante_1 = Restaurante("Can Pizza", "Italiana")
#     restaurante_2 = Restaurante("Don Chingon", "Mexicana")
#     restaurante_3 = Restaurante("El Pueblo Libre", "Peruana")
#     restaurante_4 = Restaurante("3 Focs", "Catalana")

#     for restaurante in Restaurante("nombre"):
#         if nombre not in Restaurante(nombre): 
#             print("Has hecho el error. Prueba otra vez. Escribe el nombre del restaurante para hacer la rezerva -->  ")
#         else:
#             def reservar(self, nombre, turno, cliente):
#                 if turno not in self.turnos:
#                     print(f"El turno {turno} no está disponible en {self.nombre}.")
#                     return False
                        
#                     if len(self.turnos[turno]) < 3: # check if the turn is booked
#                             self.turnos[turno].append(cliente.nombre)  # add client's name to the list
#                             print(f"Reserva realizada a {cliente.nombre} en {self.nombre} a las {turno}.")
#                             return True
#                         else:
#                             print(f"No se ha podido realizar la reserva para {cliente.nombre}. Pruebe en otro turno.")
#                             return False

    
    
#     restaurante = input("Elige el restaurante:   ")




        
#         def mostrar_reservas(self):
#             print(f"\nReservas en {self.nombre}:")
#             for turno, clientes in self.turnos.items():
#                 print(f"Turno {turno}: {', '.join(clientes) if clientes else 'Vacío'}")