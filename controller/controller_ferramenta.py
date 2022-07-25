from model.ferramenta import Ferramenta
from persistence.ferramentaDAO import FerramentaDAO
from view.view_ferramenta import ViewFerramenta
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerFerramenta(AbstractController):
    def __init__(self, controller_main):
        self.__ferramentasDAO = FerramentaDAO()
        self.__view_ferramenta = ViewFerramenta(self)
        self.__controller_main = controller_main

    @property
    def ferramentas(self):
        return self.__ferramentasDAO.pega_tudo()

    @property
    def ferramentasDAO(self):
        return self.__ferramentasDAO

    @property
    def view_ferramenta(self):
        return self.__view_ferramenta

    @property
    def controller_main(self):
        return self.__controller_main

    def incluir(self):

        while True:
            valores = self.view_ferramenta.view_incluir()
            if valores is not None:
                break
        if valores == "voltar":
            pass
        else:
            codigo = valores["codigo"]
            nome = valores["nome"]
            ferramenta = Ferramenta(nome, codigo)
            if self.ferramentasDAO.adiciona(ferramenta) is None:
                raise ObjetoDuplicadoException("uma ferramenta")
            else:
                self.view_ferramenta.pop_mensagem("✓", "Inserido com sucesso!")

    def excluir(self):
        if self.existe_obj():
            escolha_remocao = (self.
                               view_ferramenta.
                               view_codigos("ferramenta", "excluir"))
            if escolha_remocao == 'voltar':
                pass
            else:
                if (self.pega_ferramenta_pelo_codigo(
                        escolha_remocao)) is not None:
                    (self.ferramentasDAO.
                     remove(self.pega_ferramenta_pelo_codigo(escolha_remocao)))
                    (self.view_ferramenta.
                     pop_mensagem("✓", "Excluido com sucesso!"))
                else:
                    (self.view_ferramenta.
                     pop_mensagem("Erro", "Ferramenta não encontrada!"))

    def alterar(self):
        if self.existe_obj():
            escolha_edicao = (self.
                              view_ferramenta.
                              view_codigos("ferramenta", "editar"))
            if escolha_edicao == 'voltar':
                pass
            else:
                if (self.pega_ferramenta_pelo_codigo(
                        escolha_edicao)) is not None:
                    ferramenta = (self.
                                  pega_ferramenta_pelo_codigo(escolha_edicao))
                    while True:
                        novo_nome = self.view_ferramenta.view_editar()
                        if novo_nome is not None:
                            break

                    ferramenta.nome = novo_nome
                    (self.view_ferramenta.
                     pop_mensagem("✓", "Alterado com sucesso!"))
                else:
                    (self.view_ferramenta.
                     pop_mensagem("Erro", "Código não encontrado!"))

    def existe_obj(self):
        try:
            if len(self.ferramentas) == 0:
                raise ListaVaziaException("Ferramenta")
        except ListaVaziaException as e:
            self.view_ferramenta.pop_mensagem("Erro", e)
        else:
            return True

    def lista_obj_para_dict(self):
        dict = {}
        for ferramenta in self.ferramentas:
            dict[ferramenta.codigo] = str(ferramenta.nome)

        return dict

    def pega_ferramenta_pelo_codigo(self, codigo: int):
        if self.ferramentasDAO.pega(codigo) is not None:
            return self.ferramentasDAO.pega(codigo)
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar,
                    1: self.incluir,
                    2: self.excluir,
                    3: self.alterar}

        while True:
            try:
                opcao_escolhida = self.view_ferramenta.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_ferramenta.pop_mensagem("Erro", e)
