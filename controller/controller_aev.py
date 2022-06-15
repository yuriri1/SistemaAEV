from model.aev import AEV
from model.astronauta import Astronauta
from model.traje import Traje
from view.view_aev import ViewAEV

class ControllerAEV:
    def __init__(self, controller_main):
        self.__aevs = []
        self.__view_aev = ViewAEV()
        self.__manter_tela = True
        
    @property
    def aevs(self):
        return self.__aevs
    
    def selecionar_astronautas(self):
        pass
    
    def selecionar_tarefa(self):
        return self.__view_aev.listar_tarefas(self.__controller_tarefa.tarefas)
    
    def retornar(self):
        self.__manter_tela = False
    
    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.selecionar_astronautas, 
                    2: self.selecionar_tarefa, 3: self.iniciar_aev}
        
        self.__manter_tela = True
        
        while self.__manter_tela:
            opcao_escolhida = self.__view_aev.view_opcoes()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()
    
    def iniciar_aev(self):
        print("Iniciar")
        # for i in range(len(self.__controller_tarefa.tarefas)):
        #     if i == self.__controller_tarefa.tarefas[self.selecionar_tarefa()-1]:
        #         tarefa = self.__controller_tarefa.tarefas[i]
        
        # aev = AEV(1,Astronauta("Aldrin", "Americano",Traje(3,"Terreno",50.2)),tarefa)
        # self.aevs.append(aev)
        # print(self.aevs[0])