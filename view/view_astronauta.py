class ViewAstronauta:
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("========== ASTRONAUTA ===========")
        print("1 - Inserir Astronauta")
        print("2 - Remover Astronauta")
        print("3 - Editar Astronauta")
        print("4 - Listar Astronauta")
        print("0 - Voltar")
        opcao = int(input("Opcao: "))
        return opcao