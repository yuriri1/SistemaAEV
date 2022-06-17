from view.abstract_view import AbstractView

class ViewMain(AbstractView):
    def __init__(self):
        pass
    
    def menu_inicial(self):
        print("MENU INICIAL")
        print("1 - Iniciar AEV")
        print("2 - Configurar astronautas")
        print("3 - Configurar tarefa")
        print("4 - Configurar traje")
        print("5 - Configurar caixas de ferramentas")
        print("6 - Configurar ferramentas")
        print("0 - Sair")
        opcao = self.le_num_inteiro("Escolha uma opção: ",[0, 1, 2, 3, 4, 5, 6])
        return opcao