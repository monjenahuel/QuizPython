
import random

class Pregunta():
    
    def __init__(self,enunciado,categoria,re1,re2,re3,re4):
        self.categoria = categoria
        self.enunciado = enunciado
        self.re1 = re1 #re1 siempre será la respuesta correcta, su posicion será aleatoria entre las opciones
        self.re2 = re2
        self.re3 = re3
        self.re4 = re4
        self.respList = [self.re1,self.re2,self.re3,self.re4]
        self.listaDeNumerosAleatorios = random.sample(range(len(self.respList)), 4)
        self.respondidaCorrectamente = None


    def preguntar(self):
        print(self.enunciado)
        a=self.respList[self.listaDeNumerosAleatorios[0]];print("A.",a)
        b=self.respList[self.listaDeNumerosAleatorios[1]];print("B.",b)
        c=self.respList[self.listaDeNumerosAleatorios[2]];print("C.",c)
        d=self.respList[self.listaDeNumerosAleatorios[3]];print("D.",d)
        
        respuesta = None
        
        while respuesta != a and respuesta != b and respuesta != c and respuesta != d:
            respuesta = input("Elija una opcion: ")
            if respuesta.lower() == "a":
                respuesta = a
            elif respuesta.lower() == "b":
                respuesta = b
            elif respuesta.lower() == "c":
                respuesta = c
            elif respuesta.lower() == "d":
                respuesta = d
            else:
                respuesta = "None"

        self.verificarRespuesta(respuesta)

    def verificarRespuesta(self,respuesta):
        if respuesta == self.re1:
            print("¡Respuesta correcta!")
            self.respondidaCorrectamente = True
        else:
            print("Lo siento, respuesta incorrecta. Gracias por jugar")
            self.respondidaCorrectamente = False







