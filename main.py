from utils import criar_ajanela, cria_botoes, criar_frame_lista, concluir_tarefa, remove_tarefa, carrega_lista_do_json, iniciar_app

#*Cria a janela principal do programa
criar_ajanela("Minha Lista de Tarefas")

#*Cria a Tabela
criar_frame_lista("Tarefa", "Data", "Status")

#*Carrega lista do json
carrega_lista_do_json()

#*Cria o botao concluir e Remove
cria_botoes("Concluir",concluir_tarefa, 0, 2)
cria_botoes("Remove",remove_tarefa, 2, 0)

#*inicia o loop
iniciar_app()