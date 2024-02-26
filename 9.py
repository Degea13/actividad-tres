class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Depósito de", cantidad, "realizado con éxito.")
        print("Nuevo balance:", self.balance)

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes para retirar", cantidad)
        else:
            self.balance -= cantidad
            print("Retiro de", cantidad, "realizado con éxito.")
            print("Nuevo balance:", self.balance)

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Juan", "María"], 1000.0)

print("Balance inicial:", cuenta1.balance)
cuenta1.retirar(500.0)
