from model.traje import Traje
from model.tipo_traje import TipoTraje
from persistence.trajeDAO import TrajeDAO
from view.view_traje import ViewTraje
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerTraje(AbstractController):
    def __init__(self, controller_main):
        self.__trajesDAO = TrajeDAO()
        self.__view_traje = ViewTraje(self)
        self.__tipo_traje = TipoTraje
        self.__controller_main = controller_main

    @property
    def trajes(self):
        return self.__trajesDAO.pega_tudo()

    @property
    def trajesDAO(self):
        return self.__trajesDAO

    @property
    def view_traje(self):
        return self.__view_traje

    @property
    def tipo_traje(self):
        return self.__tipo_traje

    @property
    def controller_main(self):
        return self.__controller_main

    def pega_tipos(self):
        tipos = []
        for tipo in self.tipo_traje:
            tipos.append(tipo.name)
        return ";".join(tipos)

    def incluir(self):
        while True:
            valores = (self.view_traje.view_incluir(self.pega_tipos()))
            if valores is not None:
                break
        if valores == "voltar":
            pass
        else:
            codigo = valores["codigo"]
            if valores["tipo"] == "Extraveicular":
                tipo = TipoTraje.Extraveicular
            elif valores["tipo"] == "Intraveicular":
                tipo = TipoTraje.Intraveicular
            capacidade_o2 = valores["capacidade"]
            traje = Traje(codigo, tipo, capacidade_o2)
            if self.trajesDAO.adiciona(traje) is None:
                raise ObjetoDuplicadoException("um traje")
            else:
                self.view_traje.pop_mensagem("✓", "Inserido com sucesso!")

    def excluir(self):
        if self.existe_obj():
            escolha_remocao = (self.
                               view_traje.
                               view_codigos("traje", "excluir"))
            if escolha_remocao == "voltar":
                pass
            else:
                if (self.pega_traje_pelo_codigo(
                        escolha_remocao)) is not None:
                    traje = self.pega_traje_pelo_codigo(escolha_remocao)
                    if traje.dono is not None:
                        self.view_traje.pop_mensagem("Erro",
                                                     "traje com dono")
                    else:
                        self.trajesDAO.remove(traje)
                        (self.view_traje.
                         pop_mensagem("✓", "Excluido com sucesso!"))
                else:
                    (self.view_traje.
                        pop_mensagem("Erro", "Traje não encontrado!"))

    def existe_obj(self):
        try:
            if len(self.trajes) == 0:
                raise ListaVaziaException("Traje")
        except ListaVaziaException as e:
            self.view_traje.pop_mensagem("Erro", e)
        else:
            return True

    def lista_obj_para_dict(self):
        dict = {}
        for traje in self.trajes:
            if traje.dono is None:
                dict[traje.codigo] = f"{traje.tipo.name};\
{traje.capacidade_o2};Sem dono"
            else:
                dict[traje.codigo] = f"{traje.tipo.name};\
{traje.capacidade_o2};{traje.dono.nome}"

        return dict

    def pega_traje_pelo_codigo(self, codigo: int):
        if self.trajesDAO.pega(codigo) is not None:
            return self.trajesDAO.pega(codigo)
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar,
                    1: self.incluir,
                    2: self.excluir}

        while True:
            try:
                opcao_escolhida = self.view_traje.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_traje.pop_mensagem("Erro", e)
