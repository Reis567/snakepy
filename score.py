from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super(Pontuacao,self).__init__()
        self.penup()
        self.goto(0,285)
        self.pontuacao = 0
        self.hideturtle()
        self.mostra_ponto()

    def marca_ponto(self):
        self.mostra_ponto()
        self.pontuacao+=3
        
    
    def mostra_ponto(self, nome='Reis'):
        self.clear()
        self.write(f'{self.pontuacao}  |   {nome}', font=('arial', 15, 'bold'), align='center')

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f'SCORE: {self.pontuacao} , VOCÊ PERDEU',font=('arial',30,'bold'),align='center')