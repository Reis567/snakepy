import tkinter as tk
from tkinter import font
import subprocess

def jogar():
    subprocess.run(["python", "main.py"], cwd="./")

janela = tk.Tk()
janela.geometry("385x385")  # Define o tamanho da janela

# Obter as dimensões da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcular a posição x e y para centralizar a janela
pos_x = (largura_tela - 385) // 2
pos_y = (altura_tela - 385) // 2

janela.geometry(f"+{pos_x}+{pos_y}")  # Define a posição da janela
janela.configure(bg="#005440")  # Define o background da janela como verde

# Define uma fonte personalizada
fonte_titulo = font.Font(family="Arial", size=20, weight="bold")
fonte_botao = font.Font(family="Arial", size=12, weight="bold")

# Título "Snake Game"
titulo = tk.Label(janela, text="Snake Game", font=fonte_titulo, bg="#005440", fg="white")
titulo.pack(pady=10)

# Frame para centralizar os botões
frame_botoes = tk.Frame(janela, bg="#005440")
frame_botoes.pack()

# Botão Jogar
botao_jogar = tk.Button(frame_botoes, text="Jogar", command=jogar, bg="beige", font=fonte_botao, width=10, height=2, relief=tk.RAISED, bd=3)
botao_jogar.pack(side=tk.LEFT, padx=10, pady=120)

# Botão Sair
botao_sair = tk.Button(frame_botoes, text="Sair", command=janela.quit, bg="beige", font=fonte_botao, width=10, height=2, relief=tk.RAISED, bd=3)
botao_sair.pack(side=tk.LEFT, padx=10, pady=120)

janela.mainloop()