from model.traje import Traje
from model.tipo_traje import TipoTraje
from view.view_traje import ViewTraje
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerTraje:
    def __init__(self, controller_main):
        self.__trajes = []
        self.__view_traje = ViewTraje()
        self.__tipo_traje = TipoTraje

    @property
    def trajes(self):
        return self.__trajes

    @property
    def view_traje(self):
        return self.__view_traje

    def incluir(self):
        codigos = []
        codigo, tipo, capacidade_o2 = self.view_traje \
            .view_incluir(self.__tipo_traje)
        traje = Traje(codigo, tipo, capacidade_o2)
        if len(self.trajes) == 0:
            self.trajes.append(traje)
            self.view_traje.view_mensagem("Inserido com sucesso!")
        else:
            for t in self.trajes:
                codigos.append(t.codigo)
            if codigo not in codigos:
                self.trajes.append(traje)
                self.view_traje.view_mensagem("Inserido com sucesso!")
            else:
                raise ObjetoDuplicadoException("um traje")

    def excluir(self):
        if self.listar():
            codigos = []
            for traje in self.trajes:
                codigos.append(traje.codigo)
            escolha_remocao = self.view_traje.view_codigos(codigos, "excluir")
            for i, traje in enumerate(self.trajes):
                if escolha_remocao == traje.codigo:
                    self.trajes.pop(i)
                    self.view_traje.view_mensagem("Excluido com sucesso!")

    def listar(self):
        try:
            if len(self.trajes) == 0:
                raise ListaVaziaException("Traje")
        except ListaVaziaException as e:
            print(e)
        else:
            self.view_traje.view_listar(self.trajes)
            return True

    def retornar(self):
        self.__manter_tela = False
        
    def pega_traje_pelo_codigo(self, codigo):
        for traje in self.trajes:
            if traje.codigo == codigo:
                return traje
        return None

    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir,
                    2: self.excluir, 3: self.listar}

        self.__manter_tela = True

        while self.__manter_tela:
            try:
                opcao_escolhida = self.view_traje.view_opcoes()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                print(e)
