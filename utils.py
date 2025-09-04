import tkinter as tk
from tkinter import ttk
from datetime import datetime
import json
import os

ARQUIVO_JSON = "tarefas.json"

janela = None
frame_botoes = None
frame_lista = None
lista_tarefas = None
entrada_tarefa = None

def carregar_tarefas():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
                data = f.read().strip()
                return json.loads(data) if data else []
        except Exception:
            return []
    return []

def salvar_tarefas(tarefas):
    #*Salva todas as tarefas no arquivo JSON
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def adicionar_tarefa(evente=None):
    global entrada_tarefa, lista_tarefas
    titulo = entrada_tarefa.get().strip()
    if titulo:
        tarefa = {
        "titulo": titulo,
        "data": datetime.now().strftime(r"%d/%m/%Y %H:%M:%S"),
        "Status" : "Pendente"
        }
        #* Salva em JSON
        lista_tarefas.insert("", "end", values=[tarefa["titulo"],tarefa["data"],tarefa["Status"]])
        tarefas = carregar_tarefas()
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        entrada_tarefa.delete(0, tk.END)

def concluir_tarefa():
    global lista_tarefas
    for item in lista_tarefas.selection():
        valores = lista_tarefas.item(item,"values")
        lista_tarefas.item(item, values=(valores[0],valores[1], "Concluída"))
        lista_tarefas.item(item, tags=("concluida",))
        #*Atualiza no JSON
        tarefas = carregar_tarefas()
        for t in tarefas:
            if t["titulo"] == valores[0] and t["data"] == valores[1]:
                t["Status"] = "Concluída"
        salvar_tarefas(tarefas)

def remove_tarefa():
    global lista_tarefas
    for item in lista_tarefas.selection():
        valores = lista_tarefas.item(item, "values")
        lista_tarefas.delete(item)

        #*Remove também do JSON
        tarefas = carregar_tarefas()
        tarefas = [t for t in tarefas if not (t["titulo"] == valores[0] and t["data"] == valores[1])]
        salvar_tarefas(tarefas)

def criar_ajanela(titulos):
    global entrada_tarefa, janela, frame_botoes
    #*cria a janela
    janela = tk.Tk()
    janela.title(f"{titulos}")
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
    entrada_tarefa.bind("<Return>", adicionar_tarefa)
    
    #* cria uma vez o frame de botões e reusa em cria_botoes
    frame_botoes = ttk.Frame(janela)
    frame_botoes.grid(row=2, column=1, padx=5, pady=5, sticky="w")

def criar_frame_lista(coluna1, coluna2, coluna3):
    global lista_tarefas, frame_lista
    #* Frame que vai conter a lista
    frame_lista = ttk.Frame(janela,borderwidth=2, relief="solid")
    frame_lista.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    #* Configuração interna do frame
    frame_lista.grid_rowconfigure(0, weight=1)
    frame_lista.grid_columnconfigure(0, weight=1)

    #* Configuração intena na coluna
    colunas = (coluna1, coluna2, coluna3,)
    lista_tarefas = ttk.Treeview(frame_lista,columns=colunas,show="headings",height=8)
    lista_tarefas.heading(coluna1, text=coluna1, anchor="w")
    lista_tarefas.heading(coluna2, text=coluna2,)
    lista_tarefas.heading(coluna3, text=coluna3)

    #* Configura a tag de concluída
    lista_tarefas.tag_configure("concluida", font=("Arial", 9, "overstrike"))

    #* barra de rolagem
    scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_tarefas.yview)
    lista_tarefas.configure(yscrollcommand=scrollbar.set)

    lista_tarefas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def carrega_lista_do_json():
     for tarefa in carregar_tarefas():
        lista_tarefas.insert("", "end", values=[tarefa["titulo"], tarefa["data"], tarefa["Status"]])
        if tarefa["Status"] == "Concluída":
            lista_tarefas.item(lista_tarefas.get_children()[-1], tags=("concluida",))

def cria_botoes(nome_botao, comando, pixel_esquerda, pixel_direita):
    #* Cria o botao de concluir
    botao = ttk.Button(frame_botoes, text=nome_botao, command=comando)
    botao.pack(side="left", padx=(pixel_esquerda, pixel_direita))

def iniciar_app():
     janela.mainloop()
