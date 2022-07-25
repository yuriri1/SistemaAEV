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
        if self.pega(caixa.codigo) is not None:
            return None
        else:
            super().adiciona(caixa.codigo, caixa)
            return True

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, caixa: CaixaFerramenta):
        super().remove(caixa.codigo)
