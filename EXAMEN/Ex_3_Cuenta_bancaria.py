"""
Programación orientada a objetos: Gestión de cuentas bancarias.

El programa debe:

    Definir la clase Cliente, con los atributos nombre, apellido y edad.

    Definir la clase Banco, con el atributo nombre.
    Incluiremos un método "crear_cuenta" para añadir cuentas.
    Incluiremos un método "eliminar_cuenta" para quitarla del banco.
    Incluiremos el método "mostrar_cuentas" para obtener los datos
    de las diferentes cuentas y el total ingresado en el banco. Ejemplo:
    
    Banco Pasta Bank
    ==============================
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    295310 | Joan    | 4000€
    Total depósitos: 4500.0€
    ==============================


    Definir la clase CuentaBancaria con los atributos titular y saldo.
    Al crear la cuenta bancaria el saldo será 0.
    Incluiremos un número de cuenta mediante un número aleatorio entre
    100000 y 999999.

    Incluir un método ingresar_dinero(...) que permita añadir dinero a la cuenta.
    Deben ser cantidades positivas mayores que cero. En caso contrario mostrar el aviso.
    El mensaje de salida será:
    "Se han depositado [cantidad]€ en la cuenta de [nombre_del_cliente]"

    Incluir un método retirar_dinero(...) que permita retirar dinero de la cuenta, 
    si hay suficiente saldo para ello. En caso contrario, 
    mostrar un mensaje de saldo insuficiente.
    Ejemplo de mensaje: 
    "Se han retirado [cantidad]€ de la cuenta de [nombre_del_cliente]. 
    Saldo actual: [saldo]€"
    Hay que verificar que la cantidad a retirar sea positiva mayor que cero.

    Incluir un método mostrar_saldo_cliente(...) que muestre el saldo actual.
    Así:
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    
     
    Crear al menos 5 cuentas bancarias y utilizar todos 
    los métodos de cada una.

    Nota: no hace falta crear inputs para la entrada de datos.
    Se pueden utilizar directamente los métodos.
"""



import random

# Definir la clase Cliente
class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  # Nombre del cliente
        self.apellido = apellido  # Apellido del cliente
        self.edad = edad  # Edad del cliente
        self.cuentas = []  # Lista de cuentas del cliente

# Definir la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, banco):
        self.titular = titular  # Titular es un objeto Cliente
        self.saldo = 0  # Saldo inicial
        self.numero_cuenta = random.randint(100000, 999999)  # Número de cuenta aleatorio
        self.banco = banco  # Banco al que pertenece la cuenta
        titular.cuentas.append(self)  # Agregar la cuenta a la lista de cuentas del titular
    
    # Método para ingresar dinero en la cuenta especificada
    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad}€ en la cuenta de {self.titular.nombre} {self.titular.apellido}.")
        else:
            print("La cantidad a ingresar debe ser mayor que 0.")
    
    # Método para retirar dinero de la cuenta especificada
    def retirar_dinero(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad}€ de la cuenta de {self.titular.nombre} {self.titular.apellido}. Saldo actual: {self.saldo}€")
            else:
                print("Saldo insuficiente.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")
    
    # Método para mostrar saldo de la cuenta de un cliente
    def mostrar_saldo_cliente(self):
        print(f"Cuenta | Titular | Banco | Saldo")
        print(f"{self.numero_cuenta} | {self.titular.nombre} {self.titular.apellido} | {self.banco.nombre} | {self.saldo}€")

# Definir la clase Banco
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del banco
        self.cuentas = []  # Lista para guardar cuentas bancarias
    
    # Método para crear una cuenta bancaria
    def crear_cuenta(self, cliente):
        cuenta = CuentaBancaria(cliente, self)  # Crear una cuenta para el cliente en el banco
        self.cuentas.append(cuenta)
        print(f"Cuenta creada en {self.nombre} para {cliente.nombre} {cliente.apellido}. Número de cuenta: {cuenta.numero_cuenta}")
        return cuenta
    
    # Método para eliminar una cuenta bancaria
    def eliminar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                self.cuentas.remove(cuenta)
                cuenta.titular.cuentas.remove(cuenta)  # Eliminar la cuenta de la lista del cliente
                print(f"Cuenta {numero_cuenta} eliminada correctamente del banco {self.nombre}.")
                return
        print("No se encontró la cuenta.")
    
    # Método para mostrar todas las cuentas del banco
    def mostrar_cuentas(self):
        print(f"=== Banco {self.nombre} ===")
        total_depositos = 0
        for cuenta in self.cuentas:
            print(f"{cuenta.numero_cuenta} | {cuenta.titular.nombre} {cuenta.titular.apellido} | {cuenta.saldo}€")
            total_depositos += cuenta.saldo
        print(f"Total depósitos en {self.nombre}: {total_depositos}€")
        print("============================\n")
    
    # Método para buscar una cuenta por número
    def buscar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None

# Crear bancos
banco1 = Banco("Santander")
banco2 = Banco("BBVA")
banco3 = Banco("Caixa")

# Lista de clientes (simulación de base de datos)
clientes = {}

# Función para obtener un cliente, si no existe, lo crea
def obtener_cliente(nombre, apellido, edad):
    clave = (nombre.lower(), apellido.lower())  # Clave única para cada cliente
    if clave in clientes:
        return clientes[clave]
    else:
        nuevo_cliente = Cliente(nombre, apellido, edad)
        clientes[clave] = nuevo_cliente
        return nuevo_cliente

# Crear clientes y cuentas
cliente1 = obtener_cliente("Ferran", "Freddy", 30)
cuenta1 = banco1.crear_cuenta(cliente1)

cliente2 = obtener_cliente("Freddy", "America", 45)
cuenta2 = banco2.crear_cuenta(cliente2)

cliente3 = obtener_cliente("America", "Danny", 27)
cuenta3 = banco1.crear_cuenta(cliente3)
cuenta4 = banco2.crear_cuenta(cliente3)  # Misma persona, segunda cuenta en otro banco

cliente4 = obtener_cliente("Paco", "Alba", 36)
cuenta5 = banco3.crear_cuenta(cliente4)

# Función para realizar operaciones de ingreso o retiro en cuentas específicas
def operar_en_cuenta(banco, numero_cuenta, operacion, cantidad):
    cuenta = banco.buscar_cuenta(numero_cuenta)
    if cuenta:
        if operacion == "ingresar":
            cuenta.ingresar_dinero(cantidad)
        elif operacion == "retirar":
            cuenta.retirar_dinero(cantidad)
        else:
            print("Operación no válida.")
    else:
        print(f"Cuenta {numero_cuenta} no encontrada en el banco {banco.nombre}.")

# Realizar operaciones de ingreso y retiro especificando la cuenta
operar_en_cuenta(banco1, cuenta1.numero_cuenta, "ingresar", 500)
operar_en_cuenta(banco2, cuenta2.numero_cuenta, "ingresar", 4000)
operar_en_cuenta(banco1, cuenta3.numero_cuenta, "ingresar", 1200)
operar_en_cuenta(banco2, cuenta4.numero_cuenta, "ingresar", 2500)
operar_en_cuenta(banco3, cuenta1.numero_cuenta, "ingresar", 123) # Mostrará el error porque la cuenta no existe Cuenta 564886 no encontrada en el banco Caixa.

operar_en_cuenta(banco1, cuenta1.numero_cuenta, "retirar", 200)
operar_en_cuenta(banco2, cuenta2.numero_cuenta, "retirar", 500)

# Mostrar todas las cuentas de los bancos
banco1.mostrar_cuentas()
banco2.mostrar_cuentas()
banco3.mostrar_cuentas()


# Mostrar todas las cuentas de un cliente y agregar nombre del banco y saldo
print(f"Cuentas de {cliente3.nombre} {cliente3.apellido}:")
for cuenta in cliente3.cuentas:
    cuenta.mostrar_saldo_cliente()

# Eliminar una cuenta y mostrar nuevamente las cuentas del banco
banco1.eliminar_cuenta(cuenta3.numero_cuenta)
banco1.mostrar_cuentas()


