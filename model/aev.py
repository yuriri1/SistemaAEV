from model.anomalia import Anomalia
from model.astronauta import Astronauta
from model.tarefa import Tarefa


class AEV:
    def __init__(self,
                 codigo: int = None,
                 astronautas: Astronauta = None,
                 tarefa: Tarefa = None):
        self.__codigo = codigo
        self.__astronautas = astronautas
        self.__tarefa = tarefa
        self.__anomalia = None

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def astronautas(self):
        return self.__astronautas

    @astronautas.setter
    def astronautas(self, astronautas: Astronauta):
        self.__astronautas = astronautas

    @property
    def tarefa(self):
        return self.__tarefa

    @tarefa.setter
    def tarefa(self, tarefa: Tarefa):
        self.__tarefa = tarefa

    @property
    def anomalia(self):
        return self.__anomalia

    @anomalia.setter
    def anomalia(self, atributos: tuple):
        try:
            horario, tipo, descricao = atributos
        except ValueError:
            raise ValueError("Deve passar uma lista ou tupla com 3 itens")
        else:
            self.__anomalia = Anomalia(horario, tipo, descricao)
