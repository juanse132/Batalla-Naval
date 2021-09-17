import random
from warnings import simplefilter
from fila import Fila
from celda import Celda
from barco import Barco

class Tablero:
    def __init__(self):
        self.filas = [] # una lista de filas
        filascolumnas = self.preguntar_al_usuario()
        self.cantidad_de_filas = filascolumnas[0]
        self.cantidad_de_columnas = filascolumnas[1]
        self.crear_filas(self.cantidad_de_columnas)
        self.lista_barcos = []
        self.disparos = 0
    
    def crear_filas(self, cantidad_de_columnas):
        """Se crean las filas del tablero"""

        for fila in range(self.cantidad_de_filas):
            unafila = Fila(self.cantidad_de_columnas)
            self.filas.append(unafila)
    
    def preguntar_al_usuario(self):
        """Se determina las dimensiones del tablero a jugar"""

        respuesta = []
        x = input("ingrese filas del tablero ")
        if x == "":
            x = 8 
        y = input("ingrese columnas del tablero ")
        if y == "":
            y = 8
        respuesta.append(int(x))
        respuesta.append(int(y))
        return respuesta
    
    def poner_los_barcos(self):
        """Se crean los barcos y se los coloca aleatoriamente en una celda"""

       # posiciones_barcos = []
        self.barcos = int(input("ingrese la cantidad de barcos a poner: "))
        if self.barcos >= self.cantidad_de_filas * self.cantidad_de_columnas:
            print("Numero invalido, ingrese otra vez la cantidad de barcos")
            self.barcos = int(input("ingrese la cantidad de barcos a poner: "))
        else: 
            for filacolumnas in range(self.barcos):
                num_fila = random.randint(0, self.cantidad_de_filas-1)
                num_columna = random.randint(0, self.cantidad_de_columnas-1)
                unacelda = self.filas[num_fila].get_celda(num_columna)
               # posiciones_barcos.append((num_fila,num_columna))
                unBarco = Barco(True)      
                unacelda.agregar_barco(unBarco)
                self.lista_barcos.append(unBarco)

       # print(posiciones_barcos)

    def disparar(self, fila, columna):
        """Disparo a una fila y columna especifica dada por el usuario y guardo los disparos que efectuo el usuario"""

        self.filas[fila].get_celda(columna).hayBarco()
        self.disparos += 1
        return self.gane()


    def gane(self):
        """Determino si el usuario gano o sigue jugando y muestro sus disparos efectuados hasta que gano"""
        
        cantidad_barcos_vivos = self.barcos
        for barco in self.lista_barcos:
            if barco.esta_vivo():
                cantidad_barcos_vivos -= 1
        if cantidad_barcos_vivos == 0:
            print("Ganaste mi reyy, sos alto capodovich, con", self.disparos, "intentos ganaste")
            return True
        else:    
            print("Segui jugando")
            return False  


