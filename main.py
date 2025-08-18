import tkinter as tk
from tkinter import ttk

def adicionar_tarefa():
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        print("Nova tarefa:", tarefa) # debug no terminal
        lista_tarefas.insert("", "end", values=(tarefa,))
        entrada_tarefa.delete(0, tk.END)

#*cria a janela
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("400x400")

#*Cria o titulo (Minha Lista de Tarefas)
titulo = ttk.Label(janela,text="Minha Lista de Tarefas", font=("Arial",14))
titulo.pack(pady=10)

#*Cria um campo para escrever a tarefa
entrada_tarefa = ttk.Entry(janela, width=40)
entrada_tarefa.pack(pady=5)
entrada_tarefa.focus()

#*Cria o botao de adicionar
botao_adicionar = ttk.Button(janela, text="Adicionar", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)

frame_lista = ttk.Frame(janela)
frame_lista.pack(pady=10, fill="both", expand=True)


janela.mainloop()