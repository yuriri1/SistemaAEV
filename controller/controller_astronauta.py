from model.astronauta import Astronauta
from view.view_astronauta import ViewAstronauta

class ControllerAstronauta:
    def __init__(self):
        self.__astronautas = []
        self.__view_astronauta = ViewAstronauta()
        