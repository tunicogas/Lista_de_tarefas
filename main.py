import tkinter as tk
from tkinter import ttk
from datetime import datetime

dict_tarefa = []
def adicionar_tarefa(evente=None):
    titulo = entrada_tarefa.get().strip()
    if titulo:
        tarefa = {
        "titulo": titulo,
        "data": datetime.now().strftime(r"%d/%m/%Y %H:%M:%S")
        }
        print("Nova tarefa:", tarefa) # debug no terminal
        lista_tarefas.insert("", "end", values=[tarefa["titulo"],tarefa["data"]])
        dict_tarefa.append(tarefa)
        print("Todas as tarefas:", dict_tarefa)
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

#*Coluna Tarefa, Data se quiser adicionar colunas fazer nesse bloco
colunas = ("tarefa", "data",)
lista_tarefas = ttk.Treeview(frame_lista,columns=colunas,show="headings",height=8)
lista_tarefas.heading("tarefa", text="Tarefa")
lista_tarefas.heading("data", text="Data")

#* barra de rolagem
scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_tarefas.yview)
lista_tarefas.configure(yscrollcommand=scrollbar.set)

lista_tarefas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#* tecla Enter também adiciona
entrada_tarefa.bind("<Return>", adicionar_tarefa)

janela.mainloop()