class ViewCaixa:
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DA CAIXA DE FERRAMENTA")
        print("1 - Inserir Caixa de ferramentas")
        print("2 - Remover Caixa de ferramentas")
        print("3 - Editar Caixa de ferramentas")
        print("4 - Listar Caixa de ferramentas")
        print("0 - Voltar")
        opcao = int(input("Opcao: "))
        return opcao