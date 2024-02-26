import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2
    
    def calcular_lados(self):
        lado1 = abs(self.esquina1.x - self.esquina2.x)
        lado2 = abs(self.esquina1.y - self.esquina2.y)
        return lado1, lado2
    
    def calcular_perimetro(self):
        lado1, lado2 = self.calcular_lados()
        return 2 * (lado1 + lado2)
    
    def calcular_area(self):
        lado1, lado2 = self.calcular_lados()
        return lado1 * lado2
    
    def es_cuadrado(self):
        lado1, lado2 = self.calcular_lados()
        return lado1 == lado2

# Ejemplo de uso
esquina1 = Punto(1, 1)
esquina2 = Punto(4, 5)

rectangulo = Rectangulo(esquina1, esquina2)

print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())
print("Área del rectángulo:", rectangulo.calcular_area())
print("¿El rectángulo es un cuadrado?", rectangulo.es_cuadrado())
