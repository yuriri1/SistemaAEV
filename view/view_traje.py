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
        print("MENU INICIAL ---> MENU DO TRAJE --> INCLUIR TRAJE")
        codigo = self.le_num_inteiro("Codigo do traje: ")
        for i in list(tipos):
            print(str(i.value) + " - " + str(i.name))
        opcao = self.le_num_inteiro("Escolha o tipo do traje: ", [1, 2])
        for j in list(tipos):
            if opcao == j.value:
                tipo = j
        capacidade_o2 = self.le_num_flutuante("Capacidade de oxigenio: ")
        return codigo, tipo, capacidade_o2

    def view_listar(self, trajes):
        print("-"*60)
        print(f"{'CODIGO': <10}{'TIPO': ^15}\
              {'CAPACIDADE DE OXIGENIO(L)': ^20}{'DONO': >10}")
        for traje in trajes:
            if traje.dono is None:
                print(f"{traje.codigo: <10}{traje.tipo.name: ^15}\
                      {traje.capacidade_o2: >15}")
            else:
                print(f"{traje.codigo: <10}{traje.tipo.name: ^15}\
                      {traje.capacidade_o2: ^25}{traje.dono.nome: >10}")
        print("-"*60)

    def view_codigos(self, codigos: list, acao: str):
        return self.le_num_inteiro(f"Escreva o codigo do \
traje que deseja {acao}:", codigos)
