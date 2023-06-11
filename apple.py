from turtle import Turtle
import random

class Maca(Turtle):
    def __init__(self):
        super(Maca, self).__init__()  # Inicializa a classe base Turtle
        self.color('red')  # Define a cor da tartaruga como vermelho
        self.shape('circle')  # Define a forma da tartaruga como um círculo
        self.penup()  # Levanta a caneta para evitar que a tartaruga desenhe linhas
        self.shapesize(0.6)  # Define o tamanho da tartaruga como 0.6

    def nova_maca(self):
        x, y = random.randint(-280, 280), random.randint(-280, 280)  # Gera coordenadas aleatórias dentro da faixa (-280, 280)
        self.goto(x, y)  # Move a Maçã para as coordenadas geradas
