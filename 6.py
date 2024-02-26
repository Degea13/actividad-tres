class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

# Constantes para las pintas
CORAZON = "Corazón"
DIAMANTE = "Diamante"
TREBOL = "Trébol"
ESPADA = "Espada"

# Ejemplo de uso
carta1 = Carta(7, TREBOL)
carta2 = Carta(10, CORAZON)

print("Valor de la primera carta:", carta1.valor)
print("Pinta de la primera carta:", carta1.pinta)

print("Valor de la segunda carta:", carta2.valor)
print("Pinta de la segunda carta:", carta2.pinta)
