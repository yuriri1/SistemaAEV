from model.caixa_ferramenta import CaixaFerramenta
from view.view_caixa import ViewCaixa

class ControllerCaixa:
    def __init__(self):
        self.__caixas = []
        self.__view_caixa = ViewCaixa()