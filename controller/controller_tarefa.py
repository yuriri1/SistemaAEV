from model.tarefa import Tarefa
from view.view_tarefa import ViewTarefa

class ControllerTarefa:
    def __init__(self):
        self.__tarefas = []
        self.__view_tarefa = ViewTarefa()