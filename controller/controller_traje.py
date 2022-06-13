from model.traje import Traje
from view.view_traje import ViewTraje

class ControllerTraje:
    def __init__(self):
        self.__trajes = []
        self.__view_traje = ViewTraje()