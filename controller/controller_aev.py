from model.aev import AEV
from model.astronauta import Astronauta
from model.traje import Traje
from view.view_aev import ViewAEV
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException

class ControllerAEV:
    def __init__(self, controller_main):
        self.__aevs = []
        self.__view_aev = ViewAEV()
        self.__controller_main = controller_main
        self.__manter_tela = True
        
    @property
    def aevs(self):
        return self.__aevs
    
    @property
    def view_aev(self):
        return self.__view_aev
    
    @property
    def controller_main(self):
        return self.__controller_main
    
    def selecionar_astronautas(self):
        pass
    
    def selecionar_tarefa(self):
        return self.__view_aev.listar_tarefas(
                self.__controller_tarefa.tarefas)
    
    def retornar(self):
        self.__manter_tela = False
    
    def menu_opcoes(self):
        if (len(self.controller_main.controller_astronauta.astronautas) == 0 
                and len(self.controller_main.controller_tarefa.tarefas) == 0):
            raise ListaVaziaException("Astronauta e Tarefa")
        elif len(self.controller_main.controller_astronauta.astronautas) == 0:
            raise ListaVaziaException("Astronauta")
        elif len(self.controller_main.controller_tarefa.tarefas) == 0:
            raise ListaVaziaException("Tarefa")
        else:
            switcher = {0: self.retornar, 1: self.selecionar_astronautas, 
                        2: self.selecionar_tarefa, 3: self.iniciar_aev}
        
            self.__manter_tela = True
            
            while self.__manter_tela:
                opcao_escolhida = self.__view_aev.view_opcoes()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()


    def iniciar_aev(self):
        pass