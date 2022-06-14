from view.abstract_view import AbstractView

class ViewTraje(AbstractView):
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DO TRAJE")
        print("1 - Inserir traje")
        print("2 - Remover traje")
        print("3 - Listar traje")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3])
        return opcao
    
    def view_incluir(self, tipos):
        print("MENU INICIAL ---> MENU DO TRAJE --> INCLUIR")
        codigo = self.le_num_inteiro("Codigo: ")
        for i in list(tipos):
            print(str(i.value) + " - " + str(i.name))
        opcao = self.le_num_inteiro("Escolha o tipo do traje: ",[1, 2])
        for j in list(tipos):
            if opcao == j.value:
                tipo = j
        capacidade_o2 = self.le_num_flutuante("Capacidade de oxigenio: ")
        return codigo, tipo, capacidade_o2
    
    def view_listar(self, trajes):
        print("-"*50)
        print(f"{'Codigo': <10}{'tipo': ^15}{'capacidade de oxigenio(L)': >20}")
        for i in trajes:
            print(f"{i.codigo: <10}{i.tipo.name: ^15}{i.capacidade_o2: >15}")
        print("-"*50)
        
    def view_excluir(self, codigos: list):
        return self.le_num_inteiro("Escreva o codigo do \
traje que deseja excluir:", codigos)
        
    def view_mensagem(self, msg: str):
        print(msg)