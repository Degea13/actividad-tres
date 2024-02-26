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

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print("Se aplicó la cuota de manejo del 2%.")
        print("Nuevo balance después de aplicar la cuota de manejo:", self.balance)

    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Juan", "María"], 1000.0)

cuenta1.mostrar_detalles()
