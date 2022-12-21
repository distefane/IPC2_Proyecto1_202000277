class Jugador():
    def __init__(self, nombre, puntos, figura, tamaño, movimientos):
        self.nombre = nombre
        self.puntos = puntos
        self.figura = figura 
        self.tamaño = tamaño
        self.movimientos = movimientos
        self.siguiente = None