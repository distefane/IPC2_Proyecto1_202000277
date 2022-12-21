class Puzzle():
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.anterior = None
        self.arriba = None
        self.abajo = None