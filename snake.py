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
        nova_cobra.color('black')
        nova_cobra.penup()
        nova_cobra.goto(pos)
        self.corpo.append(nova_cobra)