from view.abstract_view import AbstractView

class ViewFerramenta(AbstractView):
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DA FERRAMENTA")
        print("1 - Inserir Ferramenta")
        print("2 - Remover Ferramenta")
        print("3 - Editar Ferramenta")
        print("4 - Listar Ferramenta")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ", [0,1,2,3,4])
        return opcao
    
    def view_incluir(self):
        print("MENU INICIAL ---> MENU DA FERRAMENTA --> INCLUIR FERRAMENTA")
        codigo = self.le_num_inteiro("Codigo da ferramenta: ")
        nome = str(input("Nome da ferramenta: "))
        return codigo, nome
    
    def view_listar(self, ferramentas):
        print("-"*30)
        print(f"{'CODIGO': <10}{'NOME': >20}")
        for ferramenta in ferramentas:
            print(f"{ferramenta.codigo: <20}{ferramenta.nome: >10}")
        print("-"*30)
        
    def view_codigos(self, codigos: list, acao: str):
        return self.le_num_inteiro(f"Escreva o codigo da \
ferramenta que deseja {acao}:", codigos)
        
    def view_editar(self):
        nome = str(input("Escrevao o novo nome:"))
        return nome