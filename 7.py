class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Juan", "María"], 1000.0)
cuenta2 = CuentaBancaria("987654321", ["Pedro"], 500.0)

print("Número de cuenta:", cuenta1.numero_cuenta)
print("Propietarios:", cuenta1.propietarios)
print("Balance:", cuenta1.balance)

print("Número de cuenta:", cuenta2.numero_cuenta)
print("Propietarios:", cuenta2.propietarios)
print("Balance:", cuenta2.balance)
