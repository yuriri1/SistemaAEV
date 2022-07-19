from persistence.DAO import DAO
from model.aev import AEV


class AEVDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("aev.pkl")

    def __new__(cls):
        if AEVDAO.__instance is None:
            AEVDAO.__instance = object.__new__(cls)
        return AEVDAO.__instance

    def adiciona(self, aev: AEV):
        if aev.codigo in self.__cache.keys():
            return None
        else:
            super().add(aev.codigo, aev)

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, aev: AEV):
        super().remove(aev.codigo)
