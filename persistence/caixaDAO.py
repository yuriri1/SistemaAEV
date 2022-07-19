from persistence.DAO import DAO
from model.caixa_ferramenta import CaixaFerramenta


class CaixaDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("caixa.pkl")

    def __new__(cls):
        if CaixaDAO.__instance is None:
            CaixaDAO.__instance = object.__new__(cls)
        return CaixaDAO.__instance

    def adiciona(self, caixa: CaixaFerramenta):
        if caixa.codigo in self.__cache.keys():
            return None
        else:
            super().add(caixa.codigo, caixa)

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, caixa: CaixaFerramenta):
        super().remove(caixa.codigo)
