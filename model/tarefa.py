from model.caixa_ferramenta import CaixaFerramenta


class Tarefa:
    def __init__(self, codigo: int, titulo: str,
                 descricao: str, caixa: CaixaFerramenta,
                 duracao: int):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__codigo = codigo
        self.__caixa = caixa
        self.__duracao = duracao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def caixa(self):
        return self.__caixa

    @caixa.setter
    def caixa(self, caixa: CaixaFerramenta):
        self.__caixa = caixa

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: int):
        self.__duracao = duracao
