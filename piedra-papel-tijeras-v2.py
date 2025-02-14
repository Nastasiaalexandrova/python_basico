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
opciones_juego = ["Piedra", "Papel", "Tijeras"]
opciones_juego = ['🪨','🗒️', '✂️' ]

nombre_usuario = input("Escribe tu nombre --> ")
print(f"¡Buena suerte {nombre_usuario}!")

while True:
    try:
        numero_partidas = int(input("¿Cuántas partidas quieres jugar?\n(entre 1 y 5, 0 para salir) --> "))
        if numero_partidas == 0:
            print(f"¡Hasta pronto {nombre_usuario}!")
            # os.system("exit")
            break
        elif 1<= numero_partidas <= 5:
            break
        else:
            print("Has de introducir un número entre 1 y 5\n")
    except:
        print("Has de introducir un número entero\n")


contador_de_partidas = 1

while contador_de_partidas <= numero_partidas:
    contador_de_partidas += 1
    # Informar al usuario de las opciones del juego
    menu = f"""
    PIEDRA - PAPEL - TIJERAS
    ========================

    1. {opciones_juego[0]}
    2. {opciones_juego[1]}
    3. {opciones_juego[2]}

    Escribe cualquier otra cosa para salir

    """

    print(menu)

    opcion_humano = input("Elige tu opción --> ").strip()

    if opcion_humano not in ["1","2","3"]:
        print("Juego finalizado. ¡Hasta pronto!")
    else:

        opcion_maquina = str(random.randint(1,3))

        resultado_partida = f"""
        Has elegido {opciones_juego[int(opcion_humano)-1]}
        La máquina ha elegido {opciones_juego[int(opcion_maquina)-1]}
    """
        print(resultado_partida)

        if opcion_humano == opcion_maquina:
            print(f"{nombre_usuario}, habéis empatado")
        elif (opcion_humano=="1" and opcion_maquina=="3") \
            or (opcion_humano=="2" and opcion_maquina=="1") \
                or (opcion_humano=="3" and opcion_maquina=="2"):
            print(f"{nombre_usuario} has ganado!!!")
        else:
            print(f"{nombre_usuario} has perdido!!!")

print("\nAplicación finalizada.")