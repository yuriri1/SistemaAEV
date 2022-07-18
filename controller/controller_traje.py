from model.traje import Traje
from model.tipo_traje import TipoTraje
from view.view_traje import ViewTraje
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerTraje(AbstractController):
    def __init__(self, controller_main):
        self.__trajes = []
        self.__view_traje = ViewTraje(self)
        self.__tipo_traje = TipoTraje
        self.__controller_main = controller_main

    @property
    def trajes(self):
        return self.__trajes

    @property
    def view_traje(self):
        return self.__view_traje

    @property
    def tipo_traje(self):
        return self.__tipo_traje

    @property
    def controller_main(self):
        return self.__controller_main

    def incluir(self):
        codigos = []
        codigo, tipo, capacidade_o2 = (self.
                                       view_traje.
                                       view_incluir(self.tipo_traje))
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
            escolha_remocao = (self.
                               view_traje.
                               view_codigos(codigos, "traje", "excluir"))
            for i, traje in enumerate(self.trajes):
                if escolha_remocao == traje.codigo:
                    self.trajes.pop(i)
                    self.view_traje.view_mensagem("Excluido com sucesso!")

    def listar(self):
        try:
            if len(self.trajes) == 0:
                raise ListaVaziaException("Traje")
        except ListaVaziaException as e:
            self.view_traje.pop_mensagem("Erro", e)
        else:
            self.view_traje.view_listar(self.trajes)
            return True

    def lista_obj_para_dict(self):
        lista = [Traje(1, TipoTraje.Extraveicular, 100),
                 Traje(2, TipoTraje.Intraveicular, 200)]
        dict = {}
        for traje in lista:
            dict[traje.codigo] = [traje.tipo,
                                  traje.capacidade_o2,
                                  traje.dono]

        return dict

    def pega_traje_pelo_codigo(self, codigo: int):
        for traje in self.trajes:
            if traje.codigo == codigo:
                return traje
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar,
                    1: self.incluir,
                    2: self.excluir,
                    3: self.listar}

        while True:
            try:
                opcao_escolhida = self.view_traje.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_traje.pop_mensagem("Erro", e)
