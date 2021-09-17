class Barco:
    def __init__(self, estado):
        self.estado = None
    
    def disparado(self):
        """Si el barco recibio un disparo cambio el estado del barco"""
        
        self.estado = True

    def setear_como_vivo (self):
        """Establezco que el barco esta vivo"""

        self.estado= False
    
    def esta_vivo(self):
        """Devuelvo si esta vivo o muerto dependiendo la situacion"""

        return self.estado
   