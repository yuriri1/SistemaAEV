class ViewTarefa:
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DE TAREFAS")
        print("1 - Inserir Tarefa")
        print("2 - Remover Tarefa")
        print("3 - Editar Tarefa")
        print("4 - Listar Tarefa")
        print("0 - Voltar")
        opcao = int(input("Opcao: "))
        return opcao