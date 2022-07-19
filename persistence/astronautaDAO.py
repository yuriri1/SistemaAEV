from persistence.DAO import DAO
from model.astronauta import Astronauta


class AstronautaDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("astronautas.pkl")

    def __new__(cls):
        if AstronautaDAO.__instance is None:
            AstronautaDAO.__instance = object.__new__(cls)
        return AstronautaDAO.__instance

    def adiciona(self, astronauta: Astronauta):
        if astronauta.codigo in self.__cache.keys():
            return None
        else:
            super().add(astronauta.codigo, astronauta)

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, astronauta: Astronauta):
        super().remove(astronauta.codigo)
