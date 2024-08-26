import tkinter as tk
from tkinter import ttk

# Definindo cores
COR_PRETO = "#1e1f1e"
COR_BRANCO = "#feffff"
COR_AZUL = "#38576b"
COR_CINZA = "#ECEFF1"
COR_LARANJA = "#FFAB40"

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=COR_PRETO)

# Criando frames
frame_tela = tk.Frame(janela, width=235, height=50, bg=COR_AZUL)
frame_tela.grid(row=0, column=0)

frame_corpo = tk.Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variável para armazenar todos os valores inseridos
todos_valores = ''

# Variável associada ao texto exibido na tela
valor_texto = tk.StringVar()

# Função para atualizar a tela com os valores inseridos
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

# Função para calcular o resultado da expressão
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ""

# Função para limpar a tela
def limpar_tela(): 
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Criando a label para exibir o resultado
app_label = tk.Label(
    frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, 
    relief=tk.FLAT, anchor="e", justify=tk.RIGHT, font=('Ivy 18'), 
    bg=COR_AZUL, fg=COR_BRANCO
)
app_label.place(x=0, y=0)

# Função auxiliar para criar botões
def criar_botao(frame, texto, comando, largura, altura, x, y, cor_bg, cor_fg=COR_PRETO):
    return tk.Button(
        frame, text=texto, command=comando, width=largura, height=altura,
        bg=cor_bg, fg=cor_fg, font=('Ivy 13 bold'), relief=tk.RAISED, overrelief=tk.RIDGE
    ).place(x=x, y=y)

# Criando botões
criar_botao(frame_corpo, "C", limpar_tela, 11, 2, 0, 0, COR_CINZA)
criar_botao(frame_corpo, "%", lambda: entrar_valores('%'), 5, 2, 118, 0, COR_CINZA)
criar_botao(frame_corpo, "/", lambda: entrar_valores('/'), 5, 2, 177, 0, COR_LARANJA, COR_BRANCO)

criar_botao(frame_corpo, "7", lambda: entrar_valores('7'), 5, 2, 0, 52, COR_CINZA)
criar_botao(frame_corpo, "8", lambda: entrar_valores('8'), 5, 2, 59, 52, COR_CINZA)
criar_botao(frame_corpo, "9", lambda: entrar_valores('9'), 5, 2, 118, 52, COR_CINZA)
criar_botao(frame_corpo, "*", lambda: entrar_valores('*'), 5, 2, 177, 52, COR_LARANJA, COR_BRANCO)

criar_botao(frame_corpo, "4", lambda: entrar_valores('4'), 5, 2, 0, 104, COR_CINZA)
criar_botao(frame_corpo, "5", lambda: entrar_valores('5'), 5, 2, 59, 104, COR_CINZA)
criar_botao(frame_corpo, "6", lambda: entrar_valores('6'), 5, 2, 118, 104, COR_CINZA)
criar_botao(frame_corpo, "-", lambda: entrar_valores('-'), 5, 2, 177, 104, COR_LARANJA, COR_BRANCO)

criar_botao(frame_corpo, "1", lambda: entrar_valores('1'), 5, 2, 0, 156, COR_CINZA)
criar_botao(frame_corpo, "2", lambda: entrar_valores('2'), 5, 2, 59, 156, COR_CINZA)
criar_botao(frame_corpo, "3", lambda: entrar_valores('3'), 5, 2, 118, 156, COR_CINZA)
criar_botao(frame_corpo, "+", lambda: entrar_valores('+'), 5, 2, 177, 156, COR_LARANJA, COR_BRANCO)

criar_botao(frame_corpo, "0", lambda: entrar_valores('0'), 11, 2, 0, 208, COR_CINZA)
criar_botao(frame_corpo, ".", lambda: entrar_valores('.'), 5, 2, 118, 208, COR_CINZA)
criar_botao(frame_corpo, "=", calcular, 5, 2, 177, 208, COR_LARANJA, COR_BRANCO)

# Iniciando o loop da aplicação
janela.mainloop()
