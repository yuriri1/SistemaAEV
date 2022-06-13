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
        self.__controller_aer = ControllerAEV()
        self.__controller_astronauta = ControllerAstronauta()
        self.__controller_caixa = ControllerCaixa()
        self.__controller_ferramenta = ControllerFerramenta()
        self.__controller_tarefa = ControllerTarefa()
        self.__controller_traje = ControllerTraje()
        self.__controller_anomalia = ControllerAnomalia()
        self.__view_main = ViewMain()

    def iniciar(self):
        opcao = self.__view_main.menu_inicial()

if __name__ == '__main__':
    ControllerMain().iniciar()
