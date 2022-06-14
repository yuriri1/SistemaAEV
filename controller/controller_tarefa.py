from urllib3 import Retry
from model.caixa_ferramenta import CaixaFerramenta
from model.ferramenta import Ferramenta
from model.tarefa import Tarefa
from view.view_tarefa import ViewTarefa

class ControllerTarefa:
    def __init__(self):
        self.__tarefas = [Tarefa(1,
                                 "Lavar a asa dianteira",
                                 "Colaboradores precisam ir até a asa dianteira e tirar toda poeira espacial",
                                 CaixaFerramenta(2,Ferramenta("Assoprador", 4)))]
        self.__view_tarefa = ViewTarefa()
        
    @property
    def tarefas(self):
        return self.__tarefas    
        
    def incluir(self):
        print("INCLUIR")

    def alterar(self):
        print("ALTERAR")

    def excluir(self):
        print("EXCLUIR")

    def listar(self):
        for tarefa in self.tarefas:
            print(tarefa)

    def retornar(self):
        self.__manter_tela = False
    
    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir, 
                    2: self.alterar, 3: self.excluir, 
                    4: self.listar}
        
        self.__manter_tela = True
        
        while self.__manter_tela:
            opcao_escolhida = self.__view_tarefa.view_opcoes()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()