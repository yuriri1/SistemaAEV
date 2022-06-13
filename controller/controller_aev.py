from model.aev import AEV
from view.view_aev import ViewAEV

class ControllerAEV:
    def __init__(self):
        self.__aevs = []
        self.__view_aevs = ViewAEV()
        
    def iniciar_aev(self):
        self.__view_aevs.view_opcoes()
        