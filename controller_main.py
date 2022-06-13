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

    def iniciar(self):
        # switcher = {0: False,
        #             1: self.__controller_aev.__view_aevs.view_opcoes,
        #             2: self.__controller_astronauta.__view_astronauta.view_opcoes,
        #             3: self.__controller_tarefa.__view_tarefa.view_opcoes,
        #             4: self.__controller_traje.__view_traje.view_opcoes,
        #             5: self.__controller_caixa.__view_caixa.view_opcoes,
        #             6: self.__controller_ferramenta.__view_ferramentas.view_opcoes,}
        while True:
            opcao = self.__view_main.menu_inicial()
            if opcao == 1:
                self.__controller_aev.iniciar_aev()
            elif opcao == 2:
                self.__controller_astronauta.view_opcoes()
            elif opcao == 3:
                pass
            elif opcao == 4:
                pass
            elif opcao == 5:
                pass
            elif opcao == 6:
                pass
            elif opcao == 0:
                break

if __name__ == '__main__':
    ControllerMain().iniciar()
