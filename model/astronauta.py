from model.traje import Traje


class Astronauta:
    def __init__(self, codigo: int,
                 nome: str, nacionalidade: str,
                 traje: Traje):
        self.__codigo = codigo
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__traje = traje

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        self.nacionalidade = nacionalidade

    @property
    def traje(self):
        return self.__traje

    @traje.setter
    def traje(self, traje: Traje):
        self.__traje = traje
