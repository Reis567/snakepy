from turtle import Turtle

class Campo(Turtle):
    def __init__(self):
        super(Campo, self).__init__()  # Inicializa a classe base Turtle
        self.penup()  # Levanta a caneta para evitar que a tartaruga desenhe linhas
        self.pensize(4)  # Define a espessura da caneta como 4 pixels
        self.goto(285, 285)  # Move a tartaruga para a posição (285, 285)
        self.pendown()  # Abaixa a caneta para começar a desenhar
        self.goto(285, -285)  # Desenha uma linha até a posição (285, -285)
        self.goto(-285, -285)  # Desenha uma linha até a posição (-285, -285)
        self.goto(-285, 285)  # Desenha uma linha até a posição (-285, 285)
        self.goto(285, 285)  # Desenha uma linha até a posição (285, 285)
        self.hideturtle()  # Esconde a tartaruga
