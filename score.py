from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super(Pontuacao,self).__init__()  # Inicializa a classe base Turtle
        self.penup()  # Levanta a caneta para evitar que a tartaruga desenhe linhas
        self.goto(0,285)  # Move a tartaruga para a posição (0, 285)
        self.pontuacao = 0  # Inicializa a pontuação como 0
        self.hideturtle()  # Esconde a tartaruga
        self.mostra_ponto()  # Chama o método mostra_ponto()

    def marca_ponto(self):
        self.mostra_ponto()  # Chama o método mostra_ponto()
        self.pontuacao += 3  # Aumenta a pontuação em 3 pontos
        
    
    def mostra_ponto(self, nome='Reis'):  
        self.clear()  # Limpa qualquer texto desenhado pela tartaruga
        self.write(f'{self.pontuacao}  |   {nome}', font=('arial', 15, 'bold'), align='center')  # Escreve a pontuação e o nome na tela

    def game_over(self):
        self.penup()  # Levanta a caneta
        self.goto(0, 0)  # Move a tartaruga para a posição (0, 0)
        self.write(f'SCORE: {self.pontuacao - 3} , VOCÊ PERDEU', font=('arial', 30, 'bold'), align='center')  # Escreve a pontuação final e uma mensagem de "você perdeu"
        
    def resetar_pontuacao(self):
        self.pontuacao = 0  # Zera a pontuação
        self.mostra_ponto()  # Atualiza a exibição da pontuação