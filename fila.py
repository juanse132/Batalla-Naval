from celda import Celda

class Fila:
    def __init__(self, cantidad_de_columnas):
        self.celdas = [] # una lista de celdas
        self.cantidad = cantidad_de_columnas
        self.crear_las_celdas()
    
    def crear_las_celdas(self):
        """Creo las celdas para el tablero"""

        for columna in range(self.cantidad):
            self.celdas.append(Celda())
    
    def get_celda(self, posicion):
        """Devuelvo la posicion de la celda"""
        
        return self.celdas[posicion]
    
   
        
