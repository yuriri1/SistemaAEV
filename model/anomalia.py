class Anomalia:
    def __init__(self, horario: float, tipo: str, descricao: str):
        self.__horario = horario
        self.__tipo = tipo
        self.__descricao = descricao

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: float):
        self.__horario = horario

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: float):
        self.__tipo = tipo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao
