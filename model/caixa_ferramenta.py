from model.ferramenta import Ferramenta


class CaixaFerramenta:
    def __init__(self, codigo: int, nome: str, ferramentas: Ferramenta):
        self.__codigo = codigo
        self.__nome = nome
        self.__ferramentas = ferramentas

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
    def ferramentas(self):
        return self.__ferramentas

    @ferramentas.setter
    def ferramentas(self, ferramentas: Ferramenta):
        self.__ferramentas = ferramentas
