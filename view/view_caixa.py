from view.abstract_view import AbstractView

class ViewCaixa(AbstractView):
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DA CAIXA DE FERRAMENTA")
        print("1 - Inserir Caixa de ferramentas")
        print("2 - Remover Caixa de ferramentas")
        print("3 - Listar Caixa de ferramentas")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha um opção: ", [0,1,2,3])
        return opcao
    
    def __view_ferramentas_disponiveis(self, ferramentas: list):
        print("-"*40)
        print(f"{'FERRAMENTAS DISPONIVEIS': ^40}")
        print(f"{'CODIGO': <10}{'NOME': ^15}")
        for ferramenta in ferramentas:
            print(f"{ferramenta.codigo: <10}{ferramenta.nome: ^15}")
        print("-"*40)
    
    def view_incluir(self, ferramentas: list, c_ferramenta: object):
        print("MENU INICIAL ---> MENU DA CAIXA DE FERRAMENTA\
--> INCLUIR CAIXA DE FERRAMENTA")
        codigo = self.le_num_inteiro("Codigo da caixa: ")
        nome = str(input("Nome da caixa: ")).capitalize()
        ferramentas_selecionadas = []
        print(f"O sistema possui atualmente: {len(ferramentas)} ferramentas")
        qnt_ferramenta = (self.
                          le_num_inteiro_limitado(
                              "Quantas ferramentas vão na caixa?: ",
                              len(ferramentas)))
        for i in range(qnt_ferramenta):
            self.__view_ferramentas_disponiveis(ferramentas)
            codigos = []
            for j in ferramentas:
                codigos.append(j.codigo)
            codigo_selecionado = (self.
                                  le_num_inteiro(
                                      f"Digite o codigo da {i+1}⁰ ferramenta: ",
                                      codigos))
            ferramenta_escolhida = (c_ferramenta.
                                    pega_ferramenta_pelo_codigo(
                                        codigo_selecionado))
            ferramentas_selecionadas.append(ferramenta_escolhida)
            ferramentas.remove(ferramenta_escolhida)
        
        return codigo, nome, ferramentas_selecionadas
    
    def view_listar(self, caixas: list):
        print("-"*50)
        print(f"{'CODIGO': <6}{'NOME': ^20}{'FERRAMENTAS'}")
        for caixa in caixas:
            nome_ferramentas = []
            for ferramenta in caixa.ferramentas:
                nome_ferramentas.append(ferramenta.nome)
            print(f"{caixa.codigo: <6}{caixa.nome: ^20}{', '.join(nome_ferramentas)}")
        print("-"*50)

    