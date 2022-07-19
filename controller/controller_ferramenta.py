from model.ferramenta import Ferramenta
from view.view_ferramenta import ViewFerramenta
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerFerramenta(AbstractController):
    def __init__(self, controller_main):
        self.__ferramentas = []
        self.__view_ferramenta = ViewFerramenta(self)
        self.__controller_main = controller_main

    @property
    def ferramentas(self):
        return self.__ferramentas

    @property
    def view_ferramenta(self):
        return self.__view_ferramenta

    @property
    def controller_main(self):
        return self.__controller_main

    def incluir(self):
        codigos = []
        codigo, nome = self.view_ferramenta.view_incluir()
        ferramenta = Ferramenta(nome, codigo)
        if len(self.ferramentas) == 0:
            self.ferramentas.append(ferramenta)

            self.view_ferramenta.view_mensagem("Inserido com sucesso!")
        else:
            for f in self.ferramentas:
                codigos.append(f.codigo)
            if codigo not in codigos:
                self.ferramentas.append(ferramenta)
                self.view_ferramenta.view_mensagem("Inserido com sucesso!")
            else:
                raise ObjetoDuplicadoException("uma ferramentas")

    def excluir(self):
        if self.listar():
            codigos = []
            for ferramenta in self.ferramentas:
                codigos.append(ferramenta.codigo)
            escolha_remocao = (self.
                               view_ferramenta.
                               view_codigos(codigos, "ferramenta", "excluir"))
            self.ferramentas.remove(
                self.pega_ferramenta_pelo_codigo(escolha_remocao))
            self.view_ferramenta.view_mensagem("Excluido com sucesso!")

    def alterar(self):
        if self.listar():
            codigos = []
            for ferramenta in self.ferramentas:
                codigos.append(ferramenta.codigo)
            escolha_edicao = (self.
                              view_ferramenta.
                              view_codigos(codigos, "ferramenta", "editar"))
            for ferramenta in self.ferramentas:
                if escolha_edicao == ferramenta.codigo:
                    ferramenta.nome = self.view_ferramenta.view_editar()

    def listar(self):
        try:
            if len(self.ferramentas) == 0:
                raise ListaVaziaException("Ferramenta")
        except ListaVaziaException as e:
            self.view_ferramenta.pop_mensagem("Erro", e)
        else:
            self.view_ferramenta.view_listar(self.ferramentas)
            return True

    def lista_obj_para_dict(self):
        dict = {}
        for ferramenta in self.ferramentas:
            dict[ferramenta.codigo] = str(ferramenta.nome)

        return dict

    def pega_ferramenta_pelo_codigo(self, codigo: list):
        for ferramenta in self.ferramentas:
            if ferramenta.codigo == codigo:
                return ferramenta
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar,
                    1: self.incluir,
                    2: self.excluir,
                    3: self.alterar,
                    4: self.listar}

        while True:
            try:
                opcao_escolhida = self.view_ferramenta.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_traje.pop_mensagem("Erro", e)
