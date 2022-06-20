import re
from model.aev import AEV
from model.astronauta import Astronauta
from view.view_aev import ViewAEV
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException
from exception.requisito_exception import RequisitoExcepiton

class ControllerAEV:
    def __init__(self, controller_main):
        self.__aevs = []
        self.__view_aev = ViewAEV()
        self.__controller_main = controller_main
        self.__manter_tela = True
        self.__astronautas_selecionados = []
        self.__tarefa_selecionada = []
        self.__vazao_o2 = 0.68 
        # Vazão de oxigenio em L/m baseado em:
        # https://blogs.esa.int/astronauts/2012/02/18/learning-to-spacewalk/
        # Paragrafo 5
        
    @property
    def aevs(self):
        return self.__aevs
    
    @property
    def view_aev(self):
        return self.__view_aev
    
    @property
    def controller_main(self):
        return self.__controller_main
    
    @property
    def astronautas_selecionados(self):
        return self.__astronautas_selecionados
    
    @property
    def tarefa_selecionada(self):
        return self.__tarefa_selecionada
    
    @property
    def vazao_o2(self):
        return self.__vazao_o2
    
    def selecionar_astronautas(self):
        if len(self.tarefa_selecionada) == 0:
            raise ListaVaziaException("Tarefa Selecionada")
        else:
            lista_astronautas = (self.
                                 controller_main.
                                 controller_astronauta.
                                 astronautas.copy())
            ctrl_astronauta = (self.
                               controller_main.
                               controller_astronauta)
            astronautas_escolhidos = (self.
                                        view_aev.
                                        view_selecionar_astronauta(
                                            lista_astronautas, 
                                            ctrl_astronauta))
            extraveicular = (self.controller_main.
                             controller_traje.
                             tipo_traje.
                             Extraveicular.name)
            duracao = self.tarefa_selecionada[0].duracao
            
            capacidade_o2_necessaria = (duracao*self.vazao_o2)
            
            for astronauta in astronautas_escolhidos:
                if astronauta.traje.tipo.name != extraveicular:
                    self.tarefa_selecionada = None
                    raise RequisitoExcepiton("Possuir um traje Extraveicular")
                elif (astronauta.traje.capacidade_o2 <
                      capacidade_o2_necessaria):
                    self.tarefa_selecionada.clear()
                    raise RequisitoExcepiton('''Possuir um traje com 
capacidade oxigenio adequado para a tarefa''')
                else: 
                    (self.astronautas_selecionados.
                     append(astronautas_escolhidos))
                    self.view_aev.view_mensagem('''Astronauta(s) selecionados
com sucesso!''')
    
    def selecionar_tarefa(self):
        lista_tarefas = (self.
                         controller_main.
                         controller_tarefa.
                         tarefas.copy())
        ctrl_tarefas = (self.controller_main.controller_tarefa)
        tarefas_selecionadas = (self.view_aev.
                                   view_selecionar_tarefa(
                                       lista_tarefas, ctrl_tarefas))
        self.tarefa_selecionada.append(tarefas_selecionadas)
    
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
            switcher = {0: self.retornar, 1: self.selecionar_tarefa,
                        2: self.selecionar_astronautas, 3: self.iniciar_aev}
        
            self.__manter_tela = True
            
            while self.__manter_tela:
                try:
                    opcao_escolhida = self.__view_aev.view_opcoes()
                    funcao_escolhida = switcher[opcao_escolhida]
                    funcao_escolhida()
                except ObjetoDuplicadoException as e:
                    print(e)
                except ListaVaziaException as e:
                    print(e)


    def iniciar_aev(self):
        print(self.tarefa_selecionada)