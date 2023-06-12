import tkinter as tk
from tkinter import messagebox , quit
from snake import Cobra
from apple import Maca
from score import Pontuacao

def jogar_novamente(tela):
    resposta = messagebox.askyesno("Jogo da Cobra", "Deseja jogar novamente?")
    if resposta:
        resetar_jogo()
    else:
        tk.quit()




