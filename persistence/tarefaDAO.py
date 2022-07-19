from persistence.DAO import DAO
from model.tarefa import Tarefa


class TarefaDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("tarefas.pkl")

    def __new__(cls):
        if TarefaDAO.__instance is None:
            TarefaDAO.__instance = object.__new__(cls)
        return TarefaDAO.__instance

    def adiciona(self, tarefa: Tarefa):
        if tarefa.codigo in self.__cache.keys():
            return None
        else:
            super().add(tarefa.codigo, tarefa)

    def pega(self, codigo: int):
        return super().pega(codigo)

    def remove(self, tarefa: Tarefa):
        super().remove(tarefa.codigo)
