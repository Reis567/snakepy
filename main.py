from turtle import Screen
from field import Campo
from snake import Cobra
from apple import Maca
from score import Pontuacao
import time

tela = Screen()

tela.title('Snake - By Reis567')
tela.setup(600, 620)
tela.tracer(0)
campo = Campo()
cobra = Cobra()
pontuacao = Pontuacao()
tela.listen()
tela.onkey(cobra.mover_direita, 'Right')
tela.onkey(cobra.mover_esquerda, 'Left')
tela.onkey(cobra.mover_cima, 'Up')
tela.onkey(cobra.mover_baixo, 'Down')
maca = Maca()
tela.bgcolor('beige')
jogo_on = True

while jogo_on:
    time.sleep(0.1)

    if cobra.cabeca.distance(maca)<20:
        print('Comeu uma Maçã')
        maca.nova_maca()
        cobra.crescer_cobra()
        pontuacao.marca_ponto()

    if cobra.cabeca.xcor() > 285 or \
          cobra.cabeca.xcor() < -285 or \
            cobra.cabeca.ycor() < -285 or \
                cobra.cabeca.ycor() > 285:
        pontuacao.game_over()
        jogo_on = False
        print('Perdeu')
        
    cobra.mover()
    tela.update()
tela.exitonclick()