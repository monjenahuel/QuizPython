#Hi, this is my challenge for Sofka
from jugador import *
from pregunta import *
from BancoDePreguntas import *
from records import *

class Juego():
    
    preguntaRonda = [banco.ronda1,banco.ronda2, banco.ronda3, banco.ronda4, banco.ronda5]
    
    def __init__(self):
        self.nombre = input("¿Cual es tu nombre? ")
        print("Bienvenido {}, ¿Listo para jugar?".format(self.nombre))
        self.jugadorActual = Jugador()
        self.jugar(self.jugadorActual)
        
    
    def rondaActual(self):
        return self.jugadorActual.ronda
    
    def jugar(self,jugador):
        while 0 < self.rondaActual() <= 5:
            self.preguntaRonda[self.rondaActual()-1].preguntar()
            if self.preguntaRonda[self.rondaActual()-1].respondidaCorrectamente:
                jugador.sumarPuntos()
                jugador.ronda += 1
                if self.rondaActual() <= 5:
                    print("Tenes acumulados:",jugador.puntos,"¿queres seguir jugando?(S/N)")
                    keepPlaying = None
                    while keepPlaying != "s" and keepPlaying != "n":
                        keepPlaying = input()
                        if keepPlaying.lower() == "s":
                            print("Avanzaste a la ronda",jugador.ronda)
                        elif keepPlaying.lower() == "n":
                            guardarPuntaje(self.nombre,self.jugadorActual.puntos,self.rondaActual())
                            print("Retirado exitosamente del juego")
                            input("Presione cualquier tecla para salir")
                            quit()
                else:
                    guardarPuntaje(self.nombre,self.jugadorActual.puntos,self.rondaActual())
                    print("Felicidades, ganaste el juego!")
                    print("Podes canjear tus {} puntos en la tienda".format(jugador.puntos))
                    input("Presione cualquier tecla para salir")
                    

            else:
                input("Presione cualquier tecla para salir")
                jugador.ronda = 0
    
            
         

        
game = Juego()




