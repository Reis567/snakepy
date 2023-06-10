import random
from turtle import Turtle

class cobra():
    POS_INICIAL = [(0,0) , (0,20)]
    VEL = 10
    DIREITA = 0
    ESQUERDA = 180
    CIMA = 90
    BAIXO = 270
    
    def __init__(self):
        self.corpo = []
        self.inicializar_cobra()
        self.cabeca = self.corpo[0]


    def inicializar_cobra(self):
        for pos in self.POS_INICIAL:
            self.novo_seguimento(pos)

    def novo_seguimento(self, pos):
        nova_cobra = Turtle()
        nova_cobra.shape('square')
        nova_cobra.color(random.choice(self.sorteia_cores()))
        nova_cobra.penup()
        nova_cobra.goto(pos)
        self.corpo.append(nova_cobra)
    
    def sorteia_cores(self):
        cores = ['brown','yellow','blue','purple','pink','blue','red','white','white','cyan','grey']
        return cores
    
    def mover_direita(self):
        if self.cabeca.heading() !=    self.ESQUERDA:
            self.cabeca.setheading(self.DIREITA)
            
    def mover_esquerda(self):
        if self.cabeca.heading() !=    self.DIREITA:
            self.cabeca.setheading(self.ESQUERDA)

    def mover_cima(self):
        if self.cabeca.heading() !=    self.BAIXO:
            self.cabeca.setheading(self.CIMA)

    def mover_baixo(self):
        if self.cabeca.heading() !=    self.cima:
            self.cabeca.setheading(self.BAIXO)