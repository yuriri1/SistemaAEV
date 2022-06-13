from model.ferramenta import Ferramenta
from view.view_ferramenta import ViewFerramenta

class ControllerFerramenta:
    def __init__(self):
        self.__ferramentas = []
        self.__view_ferramentas = ViewFerramenta()
