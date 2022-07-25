from persistence.DAO import DAO
from model.ferramenta import Ferramenta


class FerramentaDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("ferramentas.pkl")

    def __new__(cls):
        if FerramentaDAO.__instance is None:
            FerramentaDAO.__instance = object.__new__(cls)
        return FerramentaDAO.__instance

    def adiciona(self, ferramenta: Ferramenta):
        if self.pega(ferramenta.codigo) is not None:
            return None
        else:
            super().adiciona(ferramenta.codigo, ferramenta)
            return True

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, ferramenta: Ferramenta):
        super().remove(ferramenta.codigo)
