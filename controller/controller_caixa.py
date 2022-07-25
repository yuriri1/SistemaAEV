from model.caixa_ferramenta import CaixaFerramenta
from persistence.caixaDAO import CaixaDAO
from view.view_caixa import ViewCaixa
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerCaixa(AbstractController):
    def __init__(self, controller_main):
        self.__caixasDAO = CaixaDAO()
        self.__view_caixa = ViewCaixa(self)
        self.__controller_main = controller_main

    @property
    def caixas(self):
        return self.__caixasDAO.pega_tudo()

    @property
    def caixasDAO(self):
        return self.__caixasDAO

    @property
    def view_caixa(self):
        return self.__view_caixa

    @property
    def controller_main(self):
        return self.__controller_main

    def incluir(self):
        if len((self.controller_main.
               controller_ferramenta.ferramentas)) == 0:
            raise ListaVaziaException("Ferramenta")
        else:
            ferramentas = (self.controller_main.
                           controller_ferramenta.lista_obj_para_dict())
            while True:
                valores = self.view_caixa.view_incluir(ferramentas)
                if valores is not None:
                    break
            if valores == "voltar":
                pass
            else:
                codigo = valores["codigo"]
                nome = valores["nome"]
                codigos_ferramentas = valores["ferramentas"]
                ferramentas = []
                for codigo in codigos_ferramentas:
                    ferramentas.append(
                        self.controller_main.
                        controller_ferramenta.
                        pega_ferramenta_pelo_codigo(int(codigo)))
                caixa = CaixaFerramenta(codigo, nome, ferramentas)
                if self.caixasDAO.adiciona(caixa) is None:
                    raise ObjetoDuplicadoException("uma caixa")
                else:
                    self.view_caixa.pop_mensagem("✓", "Incluido com sucesso!")

    def excluir(self):
        if self.existe_obj():
            escolha_remocao = (self.view_caixa.
                               view_codigos("caixa", "excluir"))
            if escolha_remocao == "voltar":
                pass
            else:
                if (self.pega_caixa_pelo_codigo(
                        escolha_remocao) is not None):
                    (self.caixasDAO.
                     remove(self.pega_caixa_pelo_codigo(escolha_remocao)))
                    (self.view_caixa.
                     pop_mensagem("✓", "Excluido com sucesso!"))
                else:
                    (self.view_caixa.
                     pop_mensagem("Erro", "Caixa não encontrada"))

    def existe_obj(self):
        try:
            if len(self.caixas) == 0:
                raise ListaVaziaException("Caixa de ferramentas")
        except ListaVaziaException as e:
            self.view_caixa.pop_mensagem("Erro", e)
        else:
            return True

    def lista_obj_para_dict(self):
        dict = {}
        for caixa in self.caixas:
            lista_ferramentas = []
            for ferramenta in caixa.ferramentas:
                lista_ferramentas.append(ferramenta.nome)
            str_ferramenta = ", ".join(lista_ferramentas)

            dict[caixa.codigo] = f"{str(caixa.nome)};{str_ferramenta}"

        return dict

    def pega_caixa_pelo_codigo(self, codigo: int):
        if self.caixasDAO.pega(codigo) is not None:
            return self.caixasDAO.pega(codigo)
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir,
                    2: self.excluir}

        while True:
            try:
                opcao_escolhida = self.__view_caixa.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_caixa.pop_mensagem("Erro", e)
            except ListaVaziaException as e:
                self.view_caixa.pop_mensagem("Erro", e)
