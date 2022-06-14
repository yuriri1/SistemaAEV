from view.abstract_view import AbstractView

class ViewAstronauta(AbstractView):
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DO ASTRONAUTA")
        print("1 - Inserir Astronauta")
        print("2 - Remover Astronauta")
        print("3 - Editar Astronauta")
        print("4 - Listar Astronauta")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ",[1, 2, 3, 4, 0])
        return opcao