from model.caixa_ferramenta import CaixaFerramenta

class Tarefa:
    def __init__(self, codigo: int, titulo: str,
                 descricao: str,
                 caixas: CaixaFerramenta):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__codigo = codigo
        self.__caixas = caixas

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
    def caixas(self):
        return self.__caixas

    @caixas.setter
    def caixas(self, caixas: CaixaFerramenta):
        self.__caixas = caixas
