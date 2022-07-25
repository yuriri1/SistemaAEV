from model.astronauta import Astronauta
from persistence.astronautaDAO import AstronautaDAO
from view.view_astronauta import ViewAstronauta
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerAstronauta(AbstractController):
    def __init__(self, controller_main):
        self.__astronautasDAO = AstronautaDAO()
        self.__view_astronauta = ViewAstronauta(self)
        self.__controller_main = controller_main

    @property
    def astronautasDAO(self):
        return self.__astronautasDAO

    @property
    def astronautas(self):
        return self.__astronautasDAO.pega_tudo()

    @property
    def view_astronauta(self):
        return self.__view_astronauta

    @property
    def controller_main(self):
        return self.__controller_main

    def incluir(self):
        if len(self.controller_main.controller_traje.trajes) == 0:
            raise ListaVaziaException("Traje")
        else:
            trajes = (self.controller_main.
                      controller_traje.lista_obj_para_dict())
            trajes_disponiveis = {}
            for traje in self.controller_main.controller_traje.trajes:
                if traje.dono is None:
                    trajes_disponiveis[traje.codigo] = trajes[traje.codigo]

            while True:
                valores = self.view_astronauta.view_incluir(trajes_disponiveis)
                if valores is not None:
                    break
            if valores == "voltar":
                pass
            else:
                codigo = valores["codigo"]
                nome = valores["nome"]
                nacionalidade = valores["nacionalidade"]
                codigo_traje = int(valores["traje"])
                traje = (self.controller_main.controller_traje.
                         pega_traje_pelo_codigo(codigo_traje))
                astronauta = Astronauta(codigo, nome, nacionalidade, traje)
                traje.dono = astronauta
                self.controller_main.controller_traje.trajesDAO.altera(traje)
                if self.astronautasDAO.adiciona(astronauta) is None:
                    raise ObjetoDuplicadoException("um(a) astronauta")
                else:
                    (self.view_astronauta.
                     pop_mensagem("✓", "Incluido com sucesso!"))

    def excluir(self):
        if self.existe_obj():
            escolha_remocao = (self.view_astronauta.
                               view_codigos("astronauta", "excluir"))
            if escolha_remocao == "voltar":
                pass
            else:
                if (self.pega_astronauta_pelo_codigo(
                        escolha_remocao) is not None):
                    astro = self.pega_astronauta_pelo_codigo(escolha_remocao)
                    astro.traje.dono = None
                    self.astronautasDAO.remove(astro)
                    (self.view_astronauta.
                     pop_mensagem("✓", "Excluido com sucesso!"))
                else:
                    (self.view_astronauta.
                     pop_mensagem("Erro", "Astronauta não encontrado(a)!"))

    def existe_obj(self):
        try:
            if len(self.astronautas) == 0:
                raise ListaVaziaException("Astronauta")
        except ListaVaziaException as e:
            self.view_astronauta.pop_mensagem("Erro", e)
        else:
            return True

    def lista_obj_para_dict(self):
        dict = {}
        for astronauta in self.astronautas:
            dict[astronauta.codigo] = ((f"{astronauta.nome};") +
                                       (f"{astronauta.nacionalidade};") +
                                       (f"{astronauta.traje.tipo.name} - ") +
                                       (f"{astronauta.traje.capacidade_o2}L"))
        return dict

    def pega_astronauta_pelo_codigo(self, codigo: list):
        if self.astronautasDAO.pega(codigo) is not None:
            return self.astronautasDAO.pega(codigo)
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar,
                    1: self.incluir,
                    2: self.excluir}

        self.__manter_tela = True

        while self.__manter_tela:
            try:
                opcao_escolhida = self.__view_astronauta.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_astronauta.pop_mensagem("Erro", e)
            except ListaVaziaException as e:
                self.view_astronauta.pop_mensagem("Erro", e)
