from persistence.DAO import DAO
from model.traje import Traje


class TrajeDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("trajes.pkl")

    def __new__(cls):
        if TrajeDAO.__instance is None:
            TrajeDAO.__instance = object.__new__(cls)
        return TrajeDAO.__instance

    def adiciona(self, traje: Traje):
        if self.pega(traje.codigo) is not None:
            return None
        else:
            super().adiciona(traje.codigo, traje)
            return True

    def altera(self, traje: Traje):
        super().adiciona(traje.codigo, traje)

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, traje: Traje):
        super().remove(traje.codigo)
