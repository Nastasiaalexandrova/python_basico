'''
LISTA DE MEJORAS

Limitar un máximo de partidas
Contar cuantas veces han ganado, perdido y empatado
Preguntar el nombre del usuario

Guardar los resultados

'''



import random
import os
os.system("cls")

# Lista de las opciones
# opciones_juego = ["Piedra", "Papel", "Tijeras"]
opciones_juego = ['🪨','🗒️', '✂️' ]

partidas_ganadas = 0 # todavia tenemos 0 todo de abajo tambien
partidas_perdidas = 0
empates = 0

nombre_usuario = input("Escribe tu nombre --> ") # pedimos el nombre
print(f"¡Buena suerte {nombre_usuario}!") # mostramos el nombre

while True: # repetimos las partidas
    try:
        numero_partidas = int(input("¿Cuántas partidas quieres jugar?\n(entre 1 y 5, 0 para salir) --> ")) # preguntamos cuanto partidas quiere jugar el usuario
        if numero_partidas == 0: # si ninguna le escribimos "hasta pronto"
            print(f"¡Hasta pronto {nombre_usuario}!")
            # os.system("exit")
            break # y terminamos
        elif 1 <= numero_partidas <= 5: # numero de partidas entre 1 y 5
            break
        else:
            print("Has de introducir un número entre 1 y 5\n") # que el usuario tiene que introducir el numero
    except:
        print("Has de introducir un número entero\n") # si introduce algo otro


contador_de_partidas = 1 # el contador para saber la cantidad de juegos - 1

while contador_de_partidas <= numero_partidas:
    contador_de_partidas += 1  # subimos el contador de partidas
    # Informar al usuario de las opciones del juego
    menu = f"""
    PIEDRA - PAPEL - TIJERAS
    ========================

    1. {opciones_juego[0]}
    2. {opciones_juego[1]}
    3. {opciones_juego[2]}

    Escribe cualquier otra cosa para salir

    """

    print(menu) # imprimimos el menu

    opcion_humano = input("Elige tu opción --> ").strip() # eso es que el usuario elige entre tres opciones del partido 

    if opcion_humano not in ["1","2","3"]:
        print("Juego finalizado. ¡Hasta pronto!")  # si el usuario no ha elegido la opcion correcta
    else:

        opcion_maquina = str(random.randint(1,3)) # la maquina elige las opciones 

        resultado_partida = f"""
        Has elegido {opciones_juego[int(opcion_humano)-1]}
        La máquina ha elegido {opciones_juego[int(opcion_maquina)-1]}
    """ # imprimos los resultados del partido
        print(resultado_partida)

        if opcion_humano == opcion_maquina:
            empates += 1 # tenemos que cambiar la cantidad de empates si las opciones de maquina y el humano son al mismas
            print(f"{nombre_usuario}, habéis empatado") # mostramos el empatado
        elif (opcion_humano=="1" and opcion_maquina=="3") \
            or (opcion_humano=="2" and opcion_maquina=="1") \
                or (opcion_humano=="3" and opcion_maquina=="2"): # eligimos las opciones que ganan
            partidas_ganadas += 1 # cambiar la cantidad de las partidas
            print(f"{nombre_usuario} has ganado!!!")  # mostramos el resultado si el usuario ha ganado
        else:
            partidas_perdidas += 1 # tambien contamos la cantidad de las partidas perdidas
            print(f"{nombre_usuario} has perdido!!!") # y "saludamos" el usuario

        resultado_actual = f"""
    Ganadas: {partidas_ganadas} | Empates : {empates} | Perdidas : {partidas_perdidas}
        \n\n    
""" 
        print(resultado_actual) # mostramos el resultado del partido

print("\nAplicación finalizada.") 

