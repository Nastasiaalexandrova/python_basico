class Persona():
    """
    Propiedades de una persona
    """

    #METODOS
    # Metodo de instancia
    nombre = None
    apellido = None
    funcion = None
    def __init__(self, nombre, apellido, funcion):
        self.nombre = nombre
        self.apellido = apellido
        self.funcion = funcion


    def __str__(self):
        return f"Nombre: {self.nombre}, apellido: {self.apellido}, funcion: {self.funcion}"


# Un objeto es la instancia de una classe 
persona_1 = Persona("Peter", "Parker", "alumno")
print(type(persona_1))
persona_1.nombre = "Peter"
print(persona_1.nombre)
print(persona_1)
# print(type(persona_1.nombre))



