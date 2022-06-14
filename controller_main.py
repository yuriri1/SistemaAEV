from controller.controller_aev import ControllerAEV
from controller.controller_anomalia import ControllerAnomalia
from controller.controller_astronauta import ControllerAstronauta
from controller.controller_caixa import ControllerCaixa
from controller.controller_ferramenta import ControllerFerramenta
from controller.controller_tarefa import ControllerTarefa
from controller.controller_traje import ControllerTraje
from view.view_main import ViewMain

class ControllerMain:
    def __init__(self):
        self.__controller_aev = ControllerAEV()
        self.__controller_astronauta = ControllerAstronauta()
        self.__controller_caixa = ControllerCaixa()
        self.__controller_ferramenta = ControllerFerramenta()
        self.__controller_tarefa = ControllerTarefa()
        self.__controller_traje = ControllerTraje()
        self.__controller_anomalia = ControllerAnomalia()
        self.__view_main = ViewMain()
        self.__desliga = True


    def desligar(self):
        self.__desliga = False

    def menu_opcoes(self):
        switcher = {0: self.desligar,
                    1: self.__controller_aev.menu_opcoes,
                    2: self.__controller_astronauta.menu_opcoes,
                    3: self.__controller_tarefa.menu_opcoes,
                    4: self.__controller_traje.menu_opcoes,
                    5: self.__controller_caixa.menu_opcoes,
                    6: self.__controller_ferramenta.menu_opcoes}

        self.__desliga = True

        while self.__desliga:
            opcao = self.__view_main.menu_inicial()
            funcao_selecionada = switcher[opcao]
            funcao_selecionada()

if __name__ == '__main__':
    ControllerMain().menu_opcoes()
