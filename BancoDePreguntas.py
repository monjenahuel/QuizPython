from pregunta import *
import random

class bancoPreguntas():
    
    p1 = Pregunta("¿Cuanto es 20 + 20?",1,40,120,82,12)
    p2 = Pregunta("¿Cual es la capital de Uruguay?",1,"Montevideo","Uruguay","Entre Rios","Polonia")
    p3 = Pregunta("¿A que resolucion se le dice HD?",1,"1280x720","1920x1080","640x360","10000x10000")
    p4 = Pregunta("¿Cual es el organo más grande del cuerpo humano?",1,"La piel","El cerebro","El higado","Fosa iliaca derecha")
    p5 = Pregunta("¿172 + 188 / 55 * 0?",1,0,6.54,175,-1)

    p6 =Pregunta("¿Cuanta distancia hay de la tierra al sol?",2,"150.000.000 km","150.000.000.000 km","150.000 km","15.000")
    p7 =Pregunta("¿Cuantos Pokemon hay en la primera generacion?",2,151,251,351,51)
    p8 =Pregunta("¿De cuanto fue el viaje a Pie más largo?",2,"22.000km","2.200km","220km","220.000km")
    p9 =Pregunta("¿a cuantos cm equivalen una pulgada?",2,"2,54cm","5,48cm","10cm","0,25cm")
    p10 =Pregunta("¿Cual es el mejor gusto de helado?",2,"Frutos del Bosque","Tramontana","Vainilla","Cholocate")

    p11=Pregunta("¿Una hormiga puede levantar cuantas veces su peso?",3,8,16,4,2)
    p12=Pregunta("¿Cual es el recurso natural más abundante?",3,"El agua","La tirra","El aire","La ignorancia")
    p13=Pregunta("¿Cuantas probabilidades hay de que adivines la respuesta a una de estas preguntas?",3,"25%","50%","10%","12,75%")
    p14=Pregunta("La respuesta a esta pregunta es la B",4,"B","b","la ve","labe")
    p15=Pregunta("¿Cual de estos seres vivos sobrevivirian a un conflicto nuclear?",3,"Cucarachas","Hormigas","Cactus","Aves")

    p16=Pregunta("¿Cuantas probabilidades hay de que adivines la respuesta las 5 rondas seguidas?",4,"0,097%", "0,72%","2,14%","0,0086%")
    p17=Pregunta("¿Todas las respuestas a estas preguntas son veridicas?",4,"No","Si","Unas pocas","17 de las 25 preguntas")
    p18=Pregunta("Si la luz es tan rapida ¿Por que podemos verla?",4,"Solo vemos reflejos","Gracias a nuestra capacidad optica","No podemos verla","Solo vemos una parte")
    p19=Pregunta("¿Que es el exito?",4,"Una construccion social","Resultado de una empresa o acción emprendida, o de un suceso.","Inexistente","Todo")
    p20=Pregunta("¿Que son los años luz?",4,"Una medida de espacio","Una medida de tiempo","Una celebracion egipcia","Un suceso espacial donde interfieren las estrellas")

    p21=Pregunta("Esto es una pregunta",5,"Si","No","Tal vez","PI al cuadrado")
    p22=Pregunta("Cuantos vetices tiene un circulo",5,"Infinito","Ninguno","Si","No")
    p23=Pregunta("Segun la paradoja schrödinger...",5,"El gato esta vivo","El gato está muerto","El gato esta vivo y muerto","El gato no está vivo ni muerto")
    p24=Pregunta("¿Que ocurre si un objeto imparable impacta contra un objeto inamovible?",5,"Se atravesarian","Nada","El O.imparable pararia","El O.inamovible se moveria")
    p25=Pregunta("¿Cual de estos lenguajes es fuertemente tipado?",5,"Java","Python","Javascript","HTML")

    
    def __init__(self):
        self.listaDePreguntasR1 = [self.p1,self.p2,self.p3,self.p4,self.p5]
        self.listaDePreguntasR2 = [self.p6,self.p7,self.p8,self.p9,self.p10]
        self.listaDePreguntasR3 = [self.p11,self.p12,self.p13,self.p14,self.p15]
        self.listaDePreguntasR4 = [self.p16,self.p17,self.p18,self.p19,self.p20]
        self.listaDePreguntasR5 = [self.p21,self.p22,self.p23,self.p24,self.p25]
        
        
        self.ronda1 = self.listaDePreguntasR1[random.randint(0, 4)]
        self.ronda2 = self.listaDePreguntasR2[random.randint(0, 4)]
        self.ronda3 = self.listaDePreguntasR3[random.randint(0, 4)]
        self.ronda4 = self.listaDePreguntasR4[random.randint(0, 4)]
        self.ronda5 = self.listaDePreguntasR5[random.randint(0, 4)]

        self.preguntaRonda = [self.ronda1, self.ronda2, self.ronda3, self.ronda4, self.ronda5]

   

banco = bancoPreguntas()
