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
        if traje.codigo in self.__cache.keys():
            return None
        else:
            super().add(traje.codigo, traje)

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, traje: Traje):
        super().remove(traje.codigo)
