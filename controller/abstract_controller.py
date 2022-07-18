from abc import ABC, abstractmethod


class AbstractController(ABC):
    @abstractmethod
    def __init__(self):
        self.__manter_tela = True

    def incluir(self):
        pass

    def listar(self):
        pass

    def excluir(self):
        pass

    def alterar(self):
        pass

    def mostar_opcoes(self):
        pass

    def retornar(self):
        pass
