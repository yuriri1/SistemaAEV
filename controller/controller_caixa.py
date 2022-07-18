from model.caixa_ferramenta import CaixaFerramenta
from view.view_caixa import ViewCaixa
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerCaixa(AbstractController):
    def __init__(self, controller_main):
        self.__caixas = []
        self.__view_caixa = ViewCaixa()
        self.__controller_main = controller_main

    @property
    def caixas(self):
        return self.__caixas

    @property
    def view_caixa(self):
        return self.__view_caixa

    @property
    def controller_main(self):
        return self.__controller_main

    def incluir(self):
        lista_ferramentas = (self.
                             controller_main.
                             controller_ferramenta.
                             ferramentas.copy())
        ctrl_ferramenta = self.controller_main.controller_ferramenta
        if len(lista_ferramentas) == 0:
            raise ListaVaziaException("Ferramenta")
        else:
            codigos = []
            codigo, nome, ferramentas = (self.
                                         view_caixa.
                                         view_incluir(lista_ferramentas,
                                                      ctrl_ferramenta))
            caixa = CaixaFerramenta(codigo, nome, ferramentas)
            if len(self.caixas) == 0:
                self.caixas.append(caixa)
                self.view_caixa.view_mensagem("Inserido com sucesso!")
            else:
                for c in self.caixas:
                    codigos.append(c.codigo)
                if codigo not in codigos:
                    self.caixas.append(caixa)
                    self.view_caixa.view_mensagem("Inserido com sucesso!")
                else:
                    raise ObjetoDuplicadoException("uma ferramenta")

    def excluir(self):
        if self.listar():
            codigos = []
            for caixa in self.caixas:
                codigos.append(caixa.codigo)
            escolha_remocao = (self.view_caixa.
                               view_codigos(codigos, "caixa", "excluir"))
            self.caixas.remove(self.pega_caixa_pelo_codigo(escolha_remocao))
            self.view_caixa.view_mensagem("Excluido com sucesso!")

    def listar(self):
        try:
            if len(self.caixas) == 0:
                raise ListaVaziaException("Caixa de ferramentas")
        except ListaVaziaException as e:
            self.view_traje.pop_mensagem("Erro", e)
        else:
            self.view_caixa.view_listar(self.caixas)
            return True

    def pega_caixa_pelo_codigo(self, codigo: list):
        for caixa in self.caixas:
            if caixa.codigo == codigo:
                return caixa
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir,
                    2: self.excluir, 3: self.listar}

        while True:
            try:
                opcao_escolhida = self.__view_caixa.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_traje.pop_mensagem("Erro", e)
            except ListaVaziaException as e:
                self.view_traje.pop_mensagem("Erro", e)
