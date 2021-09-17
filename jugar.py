from tablero import Tablero

class Juego:
    def __init__ (self):
        self.eltablero = Tablero()
        self.eltablero.poner_los_barcos()
        self.jugar()

    
    def jugar (self):
        """Creo el tablero a jugar con los datos ingresados por el usuario"""
        
        columna = int(input("Ingrese a la columna que va a disparar: "))
        fila = int(input ("Ingrese a la fila que va a disparar: "))
        return self.eltablero.disparar(fila, columna)

  

if __name__=="__main__":
    unJuego = Juego()
    while True:
        if unJuego.jugar():
            break
        
