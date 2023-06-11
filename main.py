from turtle import Screen
from field import Campo
from snake import Cobra
from apple import Maca
from score import Pontuacao
import time

tela = Screen()

# Configuração da tela
tela.title('Snake - By Reis567')  # Define o título da janela do jogo
tela.setup(600, 620)  # Configura o tamanho da tela do jogo
tela.tracer(0)  # Desativa a animação automática da tela para melhorar o desempenho

campo = Campo()  # Cria o campo do jogo
cobra = Cobra()  # Cria a cobra
pontuacao = Pontuacao()  # Cria o objeto de pontuação

tela.listen()  # Habilita a escuta de eventos do teclado
tela.onkey(cobra.mover_direita, 'Right')  # Configura a tecla "Direita" para mover a cobra para a direita
tela.onkey(cobra.mover_esquerda, 'Left')  # Configura a tecla "Esquerda" para mover a cobra para a esquerda
tela.onkey(cobra.mover_cima, 'Up')  # Configura a tecla "Cima" para mover a cobra para cima
tela.onkey(cobra.mover_baixo, 'Down')  # Configura a tecla "Baixo" para mover a cobra para baixo

maca = Maca()  # Cria uma nova maçã
tela.bgcolor('beige')  # Define a cor de fundo da tela
jogo_on = True

while jogo_on:
    time.sleep(0.1)  # Pausa o programa por 0.1 segundos para controlar a velocidade do jogo

    if cobra.cabeca.distance(maca) < 20:
        print('Comeu uma Maçã')
        maca.nova_maca()  # Gera uma nova posição para a maçã
        cobra.crescer_cobra()  # Faz a cobra crescer
        pontuacao.marca_ponto()  # Incrementa a pontuação em 3 pontos

    if cobra.cabeca.xcor() > 285 or \
       cobra.cabeca.xcor() < -285 or \
       cobra.cabeca.ycor() < -285 or \
       cobra.cabeca.ycor() > 285:
        pontuacao.game_over()  # Exibe a mensagem de game over
        jogo_on = False  # Encerra o loop do jogo
        print('Perdeu')

    cobra.mover()  # Move a cobra
    tela.update()  # Atualiza a tela do jogo

tela.exitonclick()  # Fecha a janela do jogo quando o jogador clicar nela
