from controller.controller_aev import ControllerAEV
from controller.controller_astronauta import ControllerAstronauta
from controller.controller_caixa import ControllerCaixa
from controller.controller_ferramenta import ControllerFerramenta
from controller.controller_tarefa import ControllerTarefa
from controller.controller_traje import ControllerTraje
from exception.lista_vazia_exception import ListaVaziaException
from view.view_main import ViewMain


class ControllerMain:
    def __init__(self):
        self.__controller_aev = ControllerAEV(self)
        self.__controller_astronauta = ControllerAstronauta(self)
        self.__controller_caixa = ControllerCaixa(self)
        self.__controller_ferramenta = ControllerFerramenta(self)
        self.__controller_tarefa = ControllerTarefa(self)
        self.__controller_traje = ControllerTraje(self)
        self.__view_main = ViewMain()

    @property
    def controller_aev(self):
        return self.__controller_aev

    @property
    def controller_astronauta(self):
        return self.__controller_astronauta

    @property
    def controller_caixa(self):
        return self.__controller_caixa

    @property
    def controller_ferramenta(self):
        return self.__controller_ferramenta

    @property
    def controller_traje(self):
        return self.__controller_traje

    @property
    def controller_tarefa(self):
        return self.__controller_tarefa

    @property
    def controller_relatorio(self):
        return self.__controller_relatorio

    @property
    def view_main(self):
        return self.__view_main

    def opcoes_aev(self):
        self.controller_aev.menu_opcoes()

    def opcoes_astronauta(self):
        self.controller_astronauta.menu_opcoes()

    def opcoes_ferramenta(self):
        self.controller_ferramenta.menu_opcoes()

    def opcoes_caixa(self):
        self.controller_caixa.menu_opcoes()

    def opcoes_tarefa(self):
        self.controller_tarefa.menu_opcoes()

    def opcoes_traje(self):
        self.controller_traje.menu_opcoes()

    def desligar(self):
        exit(0)

    def iniciar_sistema(self):
        switcher = {0: self.desligar,
                    1: self.opcoes_aev,
                    2: self.opcoes_astronauta,
                    3: self.opcoes_tarefa,
                    4: self.opcoes_traje,
                    5: self.opcoes_caixa,
                    6: self.opcoes_ferramenta}

        while True:
            try:
                opcao_escolhida = self.view_main.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ListaVaziaException as e:
                self.view_main.pop_mensagem("Erro", e)
