class Jugador():
    def __init__(self):
        self.puntos = 0
        self.ronda = 1
        
    def cantidadDePuntos(self):
        return self.puntos

    def sumarPuntos(self):
        print("Has sumado",100 * self.ronda,"puntos")
        self.puntos =  self.puntos + 100 * self.ronda
        