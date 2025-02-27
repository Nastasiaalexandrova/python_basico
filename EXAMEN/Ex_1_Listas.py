"""
LISTAS

Escriba un programa que permita crear una lista de palabras y que, a continuación, 
pida una palabra y diga cuántas veces aparece esa palabra en la lista.

Mediante este menú:

        LISTA DE PALABRAS

        Elige una opción:
        1. Crear lista, preguntando cuantas palabras incluirá
        2. Buscar palabra
        3. Añadir palabra a la lista
        4. Borrar palabra de la lista (si existe)
        5. Mostrar la lista de palabras
        # 6. Editar la palabra que ya existe en la lista
        # 7. Borrar todas las palabras de la lista

        Cualquier otra opción para salir

        Tu elección es ....

Requerimientos:

    -- Las opciones 2-3-4-5 deben verificar que existan elementos en la lista.
        Si no hay, mostrar el correspondiente mensaje.

    -- La opción 1 siempre crea una lista nueva. Por tanto elimina la
        lista anterior si existe.

    -- Cuando se pregunte cuantas palabras incluirá la lista, no hay que
        verificar que sea un número. Se asume que el usuario escribe un número.
        Lo que sí que se debe comprobar es que sea mayor a 0.
    

Posibles mejoras:

    -- Añadir una opción para editar una palabra en la lista.
    
    -- Añadir una opción para borrar todas las palabras de la lista.

    -- Comprobar que al pedir la cantidad de palbras de la lista, el usuario
        escribe un número entero.

    -- Y lo que se te ocurra...

  
"""


# hacemos las funciones

def crear_lista():
    # Empezamos un bucle infinito para asegurar que la entrada sea válida
    while True:
        try:
            # Preguntamos cuántas palabras quiere incluir el usuario
            cantidad = int(input("Cuantas palabras incluira la lista? "))
            if cantidad > 0:
                # Si la cantidad es válida, creamos y devolvemos la lista con las palabras introducidas
                return [input(f"Palabra {i + 1}: ") for i in range(cantidad)]
            else:
                # Si la cantidad es menor o igual a 0, mostramos un mensaje de error
                print("El numero debe ser mayor a 0.")
        except ValueError:
            # Si el usuario no introduce un número entero, mostramos un mensaje de error
            print("Por favor, introduce un numero entero valido.")

def buscar_palabra(lista_palabras):
    # Verificamos si la lista está vacía
    if not lista_palabras:
        print("La lista esta vacia.")
        return
    # Pedimos la palabra que el usuario quiere buscar
    palabra = input("Introduce la palabra a buscar: ")
    # Mostramos cuántas veces aparece esa palabra en la lista
    print(f"La palabra '{palabra}' aparece {lista_palabras.count(palabra)} veces.")

def anadir_palabra(lista_palabras):
    # Pedimos la palabra que el usuario quiere añadir a la lista
    palabra = input("Introduce la palabra a añadir: ")
    # Añadimos la palabra a la lista
    lista_palabras.append(palabra)
    print(f"Palabra '{palabra}' añadida correctamente.")

def borrar_palabra(lista_palabras):
    # Verificamos si la lista está vacía
    if not lista_palabras:
        print("La lista esta vacia.")
        return
    # Pedimos la palabra que el usuario quiere borrar
    palabra = input("Introduce la palabra a borrar: ")
    # Verificamos si la palabra está en la lista y la eliminamos si es así
    if palabra in lista_palabras:
        lista_palabras.remove(palabra)
        print(f"Palabra '{palabra}' eliminada correctamente.")
    else:
        # Si la palabra no está en la lista, mostramos un mensaje de error
        print("La palabra no esta en la lista.")

def mostrar_lista(lista_palabras):
    # Verificamos si la lista está vacía
    if not lista_palabras:
        print("La lista esta vacia.")
    else:
        # Mostramos la lista de palabras
        print("Lista de palabras:", ", ".join(lista_palabras))

def editar_palabra(lista_palabras):
    # Verificamos si la lista está vacía
    if not lista_palabras:
        print("La lista esta vacia.")
        return
    # Pedimos la palabra que el usuario quiere editar
    palabra = input("Introduce la palabra que quieres editar: ")
    # Verificamos si la palabra está en la lista
    if palabra in lista_palabras:
        # Si está, pedimos la nueva palabra y la reemplazamos
        nueva_palabra = input("Introduce la nueva palabra: ")
        index = lista_palabras.index(palabra)
        lista_palabras[index] = nueva_palabra
        print("Palabra editada correctamente.")
    else:
        # Si la palabra no está en la lista, mostramos un mensaje de error
        print(f"La palabra '{palabra}' no esta en la lista.")

def borrar_todas_palabras():
    # Función para borrar todas las palabras de la lista
    return []

# Inicializamos la lista como vacía
lista_palabras = []

# Bucle principal del programa
while True:
    # Menú de opciones para el usuario
    menu = """
        Hola!
        
        Elige una opción con el numero porfavor:
        1. Crear lista, preguntando cuantas palabras incluirá
        2. Buscar palabra
        3. Añadir palabra a la lista
        4. Borrar palabra de la lista (si existe)
        5. Mostrar la lista de palabras
        6. Editar la palabra que ya existe en la lista
        7. Borrar todas las palabras de la lista
        
        Usa cualquier otra opción para salir
    """
    # Mostramos el menú en pantalla
    print(menu)
    # Pedimos al usuario que elija una opción
    opcion = input("Tu eleccion es:   ")
    
    # Dependiendo de la opción elegida, ejecutamos la función correspondiente
    if opcion == "1":
        lista_palabras = crear_lista()  # Crear lista
    elif opcion == "2":
        buscar_palabra(lista_palabras)  # Buscar palabra
    elif opcion == "3":
        anadir_palabra(lista_palabras)  # Añadir palabra
    elif opcion == "4":
        borrar_palabra(lista_palabras)  # Borrar palabra
    elif opcion == "5":
        mostrar_lista(lista_palabras)  # Mostrar lista
    elif opcion == "6":
        editar_palabra(lista_palabras)  # Editar palabra
    elif opcion == "7":
        lista_palabras = borrar_todas_palabras()  # Borrar todas las palabras
        print("Todas las palabras estan eliminadas.")
    else:
        # Si el usuario elige una opción fuera de las disponibles, salimos del programa
        print("Saliendo del programa...")
        break



