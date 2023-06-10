from turtle import Screen
from field import Campo
from snake import Cobra

tela = Screen()

tela.title('Snake - By Reis567')
tela.setup(600, 620)
tela.tracer(0)
campo = Campo()
tela.bgcolor('beige')
jogo_on = True

while jogo_on:
    tela.update()
tela.exitonclick()