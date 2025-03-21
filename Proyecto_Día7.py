from os import system
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\n Balance de Cuenta {self.numero_cuenta}: ${self.balance}"
    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print("Deposito Aceptado!")
    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos Insuficientes :(")
def crear_cliente():
    nombre_cl = input("Ingresa su nombre: ")
    apellido_cl = input("Escriba su apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente
def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 'S':
        print("Elije: Depositar (D), Retirar (R), o Salir (S)")
        opcion = input()
        if opcion == "D":
            monto_dep = int(input("Escribe el monto que quieres depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == "R":
            monto_ret = int(input("Escribe el monto que quiere retirar: "))
            mi_cliente.retirar(monto_ret)
        system("cls")
        print(mi_cliente)

    print("Gracias por USAR el Banco PAPAS")
inicio()