from view.abstract_view import AbstractView

class ViewCaixa(AbstractView):
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DA CAIXA DE FERRAMENTA")
        print("1 - Inserir Caixa de ferramentas")
        print("2 - Remover Caixa de ferramentas")
        print("3 - Editar Caixa de ferramentas")
        print("4 - Listar Caixa de ferramentas")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha um opção: ", [0,1,2,3,4])
        return opcao
    
    def __view_ferramentas_disponiveis(self, ferramentas):
        print("-"*50)
        print(f"{'FERRAMENTAS DISPONIVEIS': ^40}")
        print(f"{'CODIGO': <10}{'NOME': >20}")
        for ferramenta in ferramentas:
            print(f"{ferramenta.codigo: <20}{ferramenta.nome: >10}")
        print("-"*50)
    
    def view_incluir(self, ferramentas, c_ferramenta):
        print("MENU INICIAL ---> MENU DA CAIXA DE FERRAMENTA\
--> INCLUIR CAIXA DE FERRAMENTA")
        codigo = self.le_num_inteiro("Codigo da caixa: ")
        nome = str(input("Nome da caixa: "))
        ferramentas_selecionadas = []
        qnt_ferramenta = self\
            .le_num_inteiro_limitado("Quantas ferramentas vão na caixa?: ",
                                     len(ferramentas))
        while qnt_ferramenta > len(ferramentas):
            qnt_ferramenta = self\
            .le_num_inteiro("Quantas ferramentas vão na caixa?: ",)
        for i in range(qnt_ferramenta):
            self.__view_ferramentas_disponiveis(ferramentas)
            codigos = []
            for j in ferramentas:
                codigos.append(j.codigo)
            codigo_selecionado = self\
            .le_num_inteiro(f"Digite o codigo da {i+1}⁰ ferramenta: ", codigos)
            ferramenta_escolhida = c_ferramenta.pega_ferramenta_pelo_codigo(codigo_selecionado)
            ferramentas_selecionadas.append(ferramenta_escolhida)
            ferramentas.remove(ferramenta_escolhida)
        
        return codigo, nome, ferramentas_selecionadas
    
    def view_listar(self, caixas, n_ferramentas):
        print("-"*50)
        print(f"{'CODIGO': <10}{'NOME': ^15}{'FERRAMENTAS': >20}")
        for caixa in caixas:
            print(f"{caixa.codigo: <10}{caixa.nome: ^16}{', '.join(n_ferramentas)}")

    