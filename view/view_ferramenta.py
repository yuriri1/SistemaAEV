class ViewFerramenta:
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DA FERRAMENTA")
        print("1 - Inserir Ferramenta")
        print("2 - Remover Ferramenta")
        print("3 - Editar Ferramenta")
        print("4 - Listar Ferramenta")
        print("0 - Voltar")
        opcao = int(input("Opcao: "))
        return opcao