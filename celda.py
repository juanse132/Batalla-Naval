class Celda:
    def __init__(self):
        self.barco = None 
    
    def agregar_barco(self, barco):
        self.barco = barco  

    def hayBarco(self):
        """Determino si el usuario le da un barco o no"""
        
        if self.barco != None:
            self.barco.disparado()
            print("hundiste un barco, sos un capo")
            return True
        print("fallastee maestro")
        return False


