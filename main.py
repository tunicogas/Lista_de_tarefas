import tkinter as tk
from tkinter import ttk
from datetime import datetime
def adicionar_tarefa(evente=None):
    titulo = entrada_tarefa.get().strip()
    if titulo:
        tarefa = {
        "titulo": titulo,
        "data": datetime.now().strftime(r"%d/%m/%Y %H:%M:%S"),
        "Status" : "Pendente"
        }
        #print("Nova tarefa:", tarefa) #* debug no terminal
        lista_tarefas.insert("", "end", values=[tarefa["titulo"],tarefa["data"],tarefa["Status"]])
        entrada_tarefa.delete(0, tk.END)

def concluir_tarefa():
    for item in lista_tarefas.selection():
        valores = lista_tarefas.item(item,"values")
        lista_tarefas.item(item, values=(valores[0],valores[1], "Concluída"))
        lista_tarefas.item(item, tags=("concluida",))

def remove_tarefa():
    for item in lista_tarefas.selection():
        lista_tarefas.delete(item)
#*cria a janela
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("700x400")

#*Configuração do grid da janela
janela.grid_rowconfigure(3, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

#* Cria o titulo (Minha Lista de Tarefas)
titulo = ttk.Label(janela, text="Minha Lista de Tarefas", font=("Arial", 14))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

#* Cria um campo para escrever a tarefa
entrada_tarefa = ttk.Entry(janela, width=40)
entrada_tarefa.grid(row=1, column=0, columnspan=2, pady=5,)
entrada_tarefa.focus()

#* Frame para os botões
frame_botoes = ttk.Frame(janela)
frame_botoes.grid(row=2, column=1, padx=5, pady=5,sticky="w")

#* Cria o botao de concluir
botao_concluir = ttk.Button(frame_botoes, text="Concluir", command=concluir_tarefa)
botao_concluir.pack(side="left", padx=(0, 2))
#* Cria o botao de remove
botao_remove = ttk.Button(frame_botoes, text="remove", command= remove_tarefa)
botao_remove.pack(side="left", padx=(2, 0))

#* Frame que vai conter a lista
frame_lista = ttk.Frame(janela,borderwidth=2, relief="solid")
frame_lista.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

#* Configuração interna do frame
frame_lista.grid_rowconfigure(0, weight=1)
frame_lista.grid_columnconfigure(0, weight=1)

#* Configuração intena na coluna
colunas = ("tarefa", "data", "Status",)
lista_tarefas = ttk.Treeview(frame_lista,columns=colunas,show="headings",height=8)
lista_tarefas.heading("tarefa", text="Tarefa", anchor="w")
lista_tarefas.heading("data", text="Data",)
lista_tarefas.heading("Status", text="Status")

#* Configura a tag de concluída
lista_tarefas.tag_configure("concluida", font=("Arial", 9, "overstrike"))

#* barra de rolagem
scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_tarefas.yview)
lista_tarefas.configure(yscrollcommand=scrollbar.set)

lista_tarefas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#* tecla Enter também adiciona
entrada_tarefa.bind("<Return>", adicionar_tarefa)

janela.mainloop()
