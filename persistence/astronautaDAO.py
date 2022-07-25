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
        if self.pega(astronauta.codigo) is not None:
            return None
        else:
            super().adiciona(astronauta.codigo, astronauta)
            return True

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, astronauta: Astronauta):
        super().remove(astronauta.codigo)
