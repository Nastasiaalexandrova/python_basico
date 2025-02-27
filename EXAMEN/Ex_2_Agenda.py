"""
AGENDA

Escribir un programa que implemente una agenda.
Supondremos que siempre se indicarán nombres diferentes.

En la agenda se podrán guardar nombres y números de teléfono. 
El programa nos dará el siguiente menú:

* Añadir/modificar: Nos pide un nombre. 
    -- Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
    opcionalmente, permitir modificarlo si no es correcto, preguntando
    al usuario si quiere hacerlo. 
    -- Si el nombre no se encuentra debe añadirlo y también el teléfono correspondiente.

* Buscar: Nos pide una cadena de caracteres, 
    y nos muestras todos los contactos 
    cuyos nombres comiencen por dicha cadena.
    Por ejemplo, podemos tener contactos llamados "Mario", María", "Maria", "Mar",
    "Marta". Si buscamos "Mar" nos mostrará todos ellos. 
    Si no hay ningún contacto que comience por dicha cadena, 
    muestra el correspondiente mensaje de aviso:
    "No hay contactos que comiencen por la cadena introducida."

* Borrar: Nos pide un nombre completo y si existe nos preguntará si queremos borrarlo de la agenda. 
    Si no existe muestra el correspondiente mensaje de aviso.

* Listar: Nos muestra todos los contactos de la agenda.
    Si no hay ningún contacto, muestra el correspondiente mensaje de aviso.

* Salir, con un saludo final

Implementar el programa con un diccionario.
Como elemento de selección en el menú puedes usar letras, números o palabras completas
    (por ejemplo, "Añadir", "1", "A"), o incluso emojis.



Posibles mejoras:

* Implementar una opción en el menú que permita buscar un contacto por número de teléfono.

* Implementar el código como una función.

* Y lo que se te ocurra...

"""


def mostrar_menu(): # mostramos el menu
    menu = """
    AGENDA
    
    Elige una opción:
    1. Añadir/Modificar contacto
    2. Buscar contacto por nombre
    3. Buscar contacto por número de teléfono
    4. Borrar contacto
    5. Listar contactos
    6. Salir
    """
    print(menu)

def anadir_modificar_contacto(agenda): # creamos la funccion
    nombre = input("Introduce el nombre del contacto: ").lower() # ponemos el nombre a minusculas para guardarlo y no tener parecidas
    if nombre in agenda: # buscamos si el nombre ya existe
        print(f"El número actual de {nombre.capitalize()} es {agenda[nombre]}") # mostramos el numero del usuario elegido si existe en el diccionario
        modificar = input("¿Quieres modificarlo? (s/n): ").strip().lower() # preguntamos si quiere modificarlo otra vez
        if modificar == 's':
            telefono = input("Introduce el nuevo numero: ") # if si - modificamos
            agenda[nombre] = telefono
            print("Numero actualizado correctamente.") # y lo mostramos
    else:
        telefono = input("Introduce el numero de telefono: ") # si el nombre no esta en el diccio, lo añadimos con el numero
        agenda[nombre] = telefono
        print("Contacto añadido correctamente.") # mostramos el resultado

def buscar_contacto_por_nombre(agenda): # hacemos la funcion
    cadena = input("Introduce el inicio del nombre a buscar: ").lower() # preguntamos que quirer buscar
    encontrados = {nombre: tel for nombre, tel in agenda.items() if nombre.startswith(cadena)} # si vemos que la cadena ya esta en el dicc, lo mostramos
    if encontrados:
        for nombre, telefono in encontrados.items():
            print(f"{nombre.capitalize()}: {telefono}")
    else:
        print("No hay contactos que comiencen por la cadena introducida.") # si no hay, lo mostramos tambien

def buscar_contacto_por_telefono(agenda): # funcion para buscar el numero
    telefono = input("Introduce el numero de telefono a buscar: ")
    encontrados = [nombre for nombre, tel in agenda.items() if tel == telefono]
    if encontrados: # si lo encontramos, mostramos de quien es el numero
        for nombre in encontrados:
            print(f"El numero {telefono} pertenece a: {nombre.capitalize()}")
    else:
        print("No hay contactos con ese numero de telefono.") # si no tenemos el numero en el dicc

def borrar_contacto(agenda): # otra funcc
    nombre = input("Introduce el nombre del contacto a borrar: ").lower() # preguntamos que nomre quire borrar y si esta en el dicc, preguntamos al usuario otra vez si quiere borrarlo
    if nombre in agenda:
        confirmar = input(f"¿Seguro que quieres borrar a {nombre.capitalize()}? (s/n): ").strip().lower()
        if confirmar == 's':
            del agenda[nombre] # borramos con del(ete)
            print("Contacto eliminado correctamente.")
    else:
        print("El contacto no existe en la agenda.") # si no esta en el dicc

def listar_contactos(agenda): # funcc para mostrar la lista
    if agenda:
        for nombre, telefono in agenda.items():
            print(f"{nombre.capitalize()}: {telefono}") # mostramos los datos
    else:
        print("No hay contactos en la agenda.") # si no hay

def ejecutar_agenda(): # hacemos la funcc "major"
    agenda = {} # el dicc vacio
    while True: #usamos while para hacer las preguntas de nuevo
        mostrar_menu() # lo mostramos
        opcion = input("Tu eleccion es: ")
        
        if opcion == "1": #eligimos las opciones que el usuario quire
            anadir_modificar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto_por_nombre(agenda)
        elif opcion == "3":
            buscar_contacto_por_telefono(agenda)
        elif opcion == "4":
            borrar_contacto(agenda)
        elif opcion == "5":
            listar_contactos(agenda)
        elif opcion == "6":
            print("Gracias por usar la agenda. ¡Hasta luego!") # cerramos si no quire seguir
            break
        else:
            print("Opción no valida. Intentalo de nuevo.") # si algo incorrecto

ejecutar_agenda() #ejecutar la agenda
