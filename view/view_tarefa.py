from pydoc import describe
from model.tarefa import Tarefa
from view.abstract_view import AbstractView

class ViewTarefa(AbstractView):
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DE TAREFAS")
        print("1 - Inserir Tarefa")
        print("2 - Remover Tarefa")
        print("3 - Listar Tarefa")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ", [0,1,2,3])
        return opcao
    
    def __view_caixas_disponiveis(self, caixas: list):
        print("-"*50)
        print(f"{'CAIXAS DISPONIVEIS': ^40}")
        print(f"{'CODIGO': <10}{'NOME': ^20}{'FERRAMENTAS': >10}")
        for caixa in caixas:
            nome_ferramentas = []
            for ferramenta in caixa.ferramentas:
                nome_ferramentas.append(ferramenta.nome)
            print(f"{caixa.codigo: <10}{caixa.nome: ^20}{', '.join(nome_ferramentas): >10}")
        print("-"*50)
    
    def view_incluir(self, caixas: list, c_caixa: object):
        print("MENU INICIAL --> MENU DA TAREFAS --> INCLUIR TAREFA")
        codigo = self.le_num_inteiro("Codigo da tarefa: ")
        titulo = str(input("Titulo da tarefa: ")).capitalize()
        descricao = str(input("Descricao da tarefa: ")).capitalize()
        duracao = self.le_num_inteiro("Duracao da tarefa em minutos: ")
        self.__view_caixas_disponiveis(caixas)
        codigos = []
        for caixa in caixas:
            codigos.append(caixa.codigo)
        codigo_selecionado = (self.
                              le_num_inteiro(
                                  "Digite o codigo da caixa: ",
                                  codigos))
        caixa_escolhida = (c_caixa.
                           pega_caixa_pelo_codigo(
                               codigo_selecionado))
        
        return codigo, titulo, descricao, duracao, caixa_escolhida
    
    def view_listar(self, tarefas):
        for tarefa in tarefas:
            print("-"*50)
            print(f"{'CODIGO': <10}{'TITULO': ^15}{'CAIXA': >20}")
            print(f"{tarefa.codigo: <10}{tarefa.titulo: ^15}{tarefa.caixa.nome: >20}")
            print(f"{'DESCRIÇÃO'}")
            print(f"{tarefa.descricao}")
            print("-"*50)

        