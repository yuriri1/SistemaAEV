import ast
from view.abstract_view import AbstractView

class ViewAEV(AbstractView):
    def __init__(self):
        pass
    
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DO AEV")
        print("1 - Selecionar Tarefa")
        print("2 - Selecionar Astronautas")
        print("3 - Iniciar AEV")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ",[1, 2, 3, 0])
        return opcao
    
    def __view_astronautas_disponiveis(self, astronautas: list):
        print("-"*70)
        print(f"{'CODIGO': <10}{'NOME': ^10}\
{'NACIONALIDADE': ^15}{'TRAJE': >15}")
        for astronauta in astronautas:
            print(f"{astronauta.codigo: <10}{astronauta.nome: ^10}\
{astronauta.nacionalidade: ^15}{astronauta.traje.tipo.name: >15}")
        print("-"*70)
        
    def __view_tarefas_disponiveis(self, tarefas: list):
        for tarefa in tarefas:
            print("-"*50)
            print(f"{'CODIGO': <10}{'TITULO': ^15}{'CAIXA': >15}")
            print(f"{tarefa.codigo: <10}{tarefa.titulo: ^15}{tarefa.caixa.nome: >15}")
            print(f"{'DESCRIÇÃO'}")
            print(f"{tarefa.descricao}")
            print("-"*50)
    
    def view_selecionar_astronauta(self, astronautas: list, c_astronauta: object):
        astronautas_selecionados = []
        print(f"O sistema possui atualmente: {len(astronautas)} astronautas")
        qnt_astronautas = (self.
                           le_num_inteiro_limitado(
                               "Quantos astronautas vão na AEV?: ",
                               len(astronautas)))
        for i in range(qnt_astronautas):
            self.__view_astronautas_disponiveis(astronautas)
            codigos = []
            for astronauta in astronautas:
                codigos.append(astronauta.codigo)
            codigo_selecionado = (self.
                                  le_num_inteiro(
                                      f"Digite o codigo do {i+1}º astronauta",
                                      codigos))
            astronauta_escolhido = (c_astronauta.
                                    pega_astronauta_pelo_codigo(
                                        codigo_selecionado))
            astronautas_selecionados.append(astronauta_escolhido)
            astronautas.remove(astronauta_escolhido)
        return astronautas_selecionados
    
    def view_selecionar_tarefa(self, tarefas: list, c_tarefa: object):
        self.__view_tarefas_disponiveis(tarefas)
        codigos = []
        for tarefa in tarefas:
            codigos.append(tarefa.codigo)
        codigo_selecionado = (self.
                                le_num_inteiro(
                                    f"Digite o codigo da tarefa: ",
                                    codigos))
        tarefa_selecionada = (c_tarefa.
                              pega_tarefa_pelo_codigo(
                                  codigo_selecionado))
        return tarefa_selecionada
       
    
    def view_relatar_anomalia(self):
        print("MENU INICIAL --> MENU DO AEV --> AEV EM EXECUÇÃO -->\
RELATANDO ANOMALIA")
        horario = input("Quando ocorreu a anomalia: ")
        tipo = input("Tipo da anomalia: ")
        descricao = input("Descreva a ocorrencia: ")
        return horario, tipo, descricao
        