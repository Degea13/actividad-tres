import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print("Coordenadas del punto: ({}, {})".format(self.x, self.y))
    
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
    
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

# Ejemplo de uso
punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

punto1.mostrar()
punto2.mostrar()

nuevo_x = 5
nuevo_y = 7
punto1.mover(nuevo_x, nuevo_y)

punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print("La distancia entre punto1 y punto2 es:", distancia)
