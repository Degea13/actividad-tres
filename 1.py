class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

# Ejemplo de uso
mi_coche = Vehiculo(200, 50000)  # Creamos un objeto Vehiculo con una velocidad máxima de 200 y un kilometraje de 50000
print("Velocidad máxima:", mi_coche.velocidad_maxima)
print("Kilometraje:", mi_coche.kilometraje)
