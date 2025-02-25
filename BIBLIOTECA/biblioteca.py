"""
Programación Orientada a Objetos: Biblioteca

El programa debe crear las siguientes clases con sus métodos:

    Clase Lector, que se construirá con nombre y apellido

    Clase Libro, que se construirá con nombre_autor, apellido_autor,
    y título

    Clase Biblioteca, que se construirá con nombre y dirección
    Esta clase dispondrá de los siguientes métodos:
    - agregar_lector: agrega un lector a la biblioteca
    - mostrar lectores
    - agregar_libro: agrega un libro a la biblioteca,
        indicando los ejemplare disponibles
    - buscar_libro: busca un libro en la biblioteca, 
        indicando si lo tiene o no
    - mostrar libros de la biblioteca


"""

class Lector:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro:
    def __init__(self, nombre_autor, apellido_autor, titulo):
        self.nombre = nombre_autor
        self.apellido = apellido_autor
        self.titulo = titulo
        self.cantidad = 0
    
    def __str__(self):
        return f"{self.nombre} de {self.apellido} {self.titulo}, {self.cantidad}"

class Biblioteca:
    def __init__(self, nombre_bibl, direccion):
        self.nombre = nombre_bibl
        self.direccion = direccion
        self.lectores = []

    def agregar_lector(self, nombre, apellido):
        # Check if the reader already exists in the list
        for lector in self.lectores:
            if lector.nombre == nombre and lector.apellido == apellido:
                print(f"El lector {nombre} {apellido} ya existe. Pruebe hacerlo de nuevo")
                return  # This immediately stops the rest of the function and prevents further code execution
                
        # If the reader is not in the list, add them
        self.lectores.append(Lector(nombre, apellido))
        print(f"El usuario {nombre} {apellido} está añadido.")

    def mostrar_lectores(self):
        print("La lista de lectores:")
        for lector in self.lectores:
            print(lector)

    def agregar_libro(self, libro, cantidad):
        libro.cantidad = cantidad
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' de {libro.nombre} {libro.apellido} se ha añadido a la biblioteca.")
        
    def mostrar_libros(self, libro, cantidad):
        print("La lista de los libros: \n")
        for libro in libros:
            print(f"{self.nombre_autor} {self.apellido_autor} {self.titulo} {self.cantidad}\n")
        

# Create the Biblioteca object
biblioteca = Biblioteca("Central", "carrer Corsega 409, Barcelona")

# Adding readers to the list
biblioteca.agregar_lector("Anastasiia", "Mishakova")
biblioteca.agregar_lector("Juan", "Perez")
biblioteca.agregar_lector("Aniia", "Misha")
biblioteca.agregar_lector("Anastasiia", "Mishakova")  

# Show all readers
biblioteca.mostrar_lectores()

libro_1 = Libro("Qereti", "Juan Juaaa", "Kkjgasdkai", 2)

libro1 = Libro("Stephen", "King", "It")
libro2 = Libro("J.R.R.", "Tolkien", "El Señor de los Anillos")
biblioteca.agregar_libro(libro1, 5)
biblioteca.agregar_libro(libro2, 3)










# class Lector:
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido

# class Libro:
#     def __init__(self, nombre_autor, apellido_autor, titulo):
#         self.nombre_autor = nombre_autor
#         self.apellido_autor = apellido_autor
#         self.titulo = titulo

# class Biblioteca:
#     def __init__(self, nombre, direccion):
#         self.nombre = nombre
#         self.direccion = direccion
#         self.lectores = []
#         self.libros = []

#     def agregar_lector(self, lector):
#         self.lectores.append(lector)    

#     def mostrar_lectores(self):
#         for lector in self.lectores:
#             print(lector.nombre, lector.apellido)
        
#     def agregar_libro(self, libro, ejemplares):
#         self.libros.append((libro, ejemplares))

#     def buscar_libro(self, titulo):
#         for libro in self.libros:
#             if libro[0].titulo == titulo:
#                 print(f"El libro {titulo} está en la biblioteca")
#                 return
#         print(f"El libro {titulo} no está en la biblioteca")

#     def mostrar_libros(self):
#         for libro in self.libros:
#             print(libro[0].titulo, libro[1])
        
#         if __name__ == "__main__":
#             lector1 = Lector("Juan", "Pérez")
#             lector2 = Lector("María", "Gómez")
#             libro1 = Libro("Stephen", "King", "It")
#             libro2 = Libro("J.R.R.", "Tolkien", "El Señor de los Anillos")
#             biblioteca = Biblioteca("Biblioteca Municipal", "Calle Mayor, 1")
#             biblioteca.agregar_lector(lector1)
#             biblioteca.agregar_lector(lector2)
#             biblioteca.mostrar_lectores()
#             biblioteca.agregar_libro(libro1, 5)
#             biblioteca.agregar_libro(libro2, 3)
#             biblioteca.mostrar_libros()
#             biblioteca.buscar_libro("It")
#             biblioteca.buscar_libro("El Señor de los Anillos")
#             biblioteca.buscar_libro("El Quijote")
# """
# # Test
# # Lector
# lector1 = Lector("Juan", "Pérez")
# lector2 = Lector("María", "Gómez")
# assert lector1.nombre == "Juan"
# assert lector1.apellido == "Pérez"
# assert lector2.nombre == "María"
# assert lector2.apellido == "Gómez"
# """

