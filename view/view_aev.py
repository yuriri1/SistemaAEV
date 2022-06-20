import random
import time
from view.abstract_view import AbstractView


class ViewAEV(AbstractView):
    def __init__(self):
        pass

    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DO AEV")
        print("1 - Iniciar AEV")
        print("2 - Selecionar Astronautas")
        print("3 - Selecionar Tarefa")
        print("4 - Listar AEV's")
        print("5 - Gerar relatorio")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 0])
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
            print(f"{tarefa.codigo: <10}{tarefa.titulo: ^15}\
{tarefa.caixa.nome: >15}")
            print(f"{'DESCRIÇÃO'}")
            print(f"{tarefa.descricao}")
            print("-"*50)

    def view_selecionar_astronauta(self, astronautas: list,
                                   c_astronauta: object):
        astronautas_selecionados = []
        print(f"O sistema possui atualmente: {len(astronautas)} astronautas")
        if len(astronautas) == 1:
            qnt_astronautas = (self.le_num_inteiro_limitado(
                                "Quantos astronautas vão na AEV?(Max 1): ", 1))
        elif len(astronautas) > 1:
            qnt_astronautas = (self.le_num_inteiro_limitado(
                                "Quantos astronautas vão na AEV?(Max 2): ", 2))
        for i in range(qnt_astronautas):
            self.__view_astronautas_disponiveis(astronautas)
            codigos = []
            for astronauta in astronautas:
                codigos.append(astronauta.codigo)
            codigo_selecionado = (self.
                                  le_num_inteiro(
                                      f"Digite o codigo\
do {i+1}º astronauta: ", codigos))
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
                              le_num_inteiro("Digite o codigo da tarefa: ",
                                             codigos))
        tarefa_selecionada = (c_tarefa.
                              pega_tarefa_pelo_codigo(
                                  codigo_selecionado))
        return tarefa_selecionada

    def view_aev_andamento(self, codigo):
        chars = ["¨"]
        for i in range(10):
            for j in range(random.randint(5, 20)):
                print(random.choice(chars), end='')
            time.sleep(1)
            print()
        print(f"MISSÃO AEV Nº{codigo} EM ANDAMENTO")
        print("1 - Encerrar AEV")
        print("2 - Relatar anomalia")
        opcao = self.le_num_inteiro("Escolha uma opção: ", [1, 2])
        return opcao

    def view_listar(self, aevs):
        print("-"*6)
        print("CODIGO")
        for aev in aevs:
            print(aev.codigo)
        print("-"*6)

    def view_relatar_anomalia(self, tarefa):
        print("MENU INICIAL --> MENU DO AEV --> AEV EM EXECUÇÃO -->\
RELATANDO ANOMALIA")
        horario = self.le_num_inteiro_limitado(
            "Em que minuto ocorreu a anomalia: ", tarefa.duracao)
        tipo = input("Tipo da anomalia: ")
        descricao = input("Descreva a ocorrencia: ")
        return horario, tipo, descricao
