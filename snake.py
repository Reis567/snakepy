import random
from turtle import Turtle

class Cobra():
    POS_INICIAL = [(0,0) , (0,20),  (0,40),  (0,60)]  # Posição inicial da cobra
    VEL = 10  # Velocidade da cobra
    DIREITA = 0  # Constante para a direção direita
    ESQUERDA = 180  # Constante para a direção esquerda
    CIMA = 90  # Constante para a direção para cima
    BAIXO = 270  # Constante para a direção para baixo
    
    def __init__(self):
        self.corpo = []  # Lista para armazenar os segmentos da cobra
        self.inicializar_cobra()  # Inicializa a cobra
        self.cabeca = self.corpo[0]  # Referência para a cabeça da cobra
    
    def mover(self):
        for index in range(len(self.corpo)-1, 0, -1):  # Percorre os segmentos da cobra, começando pelo último
            novo_x, novo_y = self.corpo[index-1].xcor(), self.corpo[index-1].ycor()  # Obtém as coordenadas do segmento anterior
            self.corpo[index].goto(novo_x, novo_y)  # Move o segmento atual para as novas coordenadas
        self.cabeca.forward(self.VEL)  # Move a cabeça da cobra para frente

    def inicializar_cobra(self):
        for pos in self.POS_INICIAL:  # Percorre as posições iniciais da cobra
            self.novo_seguimento(pos)  # Cria um novo segmento da cobra na posição

    def novo_seguimento(self, pos):
        nova_cobra = Turtle()
        nova_cobra.shape('square')  # Define a forma do segmento como um quadrado
        nova_cobra.color(random.choice(self.sorteia_cores()))  # Escolhe uma cor aleatória para o segmento
        nova_cobra.penup()  # Levanta a caneta para evitar que a tartaruga desenhe linhas
        nova_cobra.goto(pos)  # Move o segmento para a posição especificada
        self.corpo.append(nova_cobra)  # Adiciona o segmento à lista de segmentos da cobra

    def crescer_cobra(self):
        last_segment = self.corpo[-1]  # Obtém o último segmento da cobra
        x, y = last_segment.position()  # Obtém as coordenadas do último segmento
        self.novo_seguimento((x, y))  # Cria um novo segmento da cobra na posição do último segmento

    def sorteia_cores(self):
        cores = ['brown', 'yellow', 'blue', 'purple', 'pink', 'blue', 'red', 'white', 'white', 'cyan', 'grey', 'green', 'orange', 'magenta', 'gold', 'teal', 'lavender', 'coral', 'silver', 'maroon']
        return cores


    def mover_direita(self):
        if self.cabeca.heading() != self.ESQUERDA:  # Verifica se a cobra não está indo para a esquerda
            self.cabeca.setheading(self.DIREITA)  # Define a direção da cabeça da cobra para a direita


    def mover_esquerda(self):
        if self.cabeca.heading() != self.DIREITA:  # Verifica se a cobra não está indo para a direita
            self.cabeca.setheading(self.ESQUERDA)  # Define a direção da cabeça da cobra para a esquerda

    def mover_cima(self):
        if self.cabeca.heading() != self.BAIXO:  # Verifica se a cobra não está indo para baixo
            self.cabeca.setheading(self.CIMA)  # Define a direção da cabeça da cobra para cima

    def mover_baixo(self):
        if self.cabeca.heading() != self.CIMA:  # Verifica se a cobra não está indo para cima
            self.cabeca.setheading(self.BAIXO)  # Define a direção da cabeça da cobra para baixo
