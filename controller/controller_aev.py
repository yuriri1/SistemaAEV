from model.aev import AEV
from persistence.aevDAO import AEVDAO
from view.view_aev import ViewAEV
from controller.abstract_controller import AbstractController
from relatorios.relatorio import Relatorio
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException
from exception.requisito_exception import RequisitoExcepiton


class ControllerAEV(AbstractController):
    def __init__(self, controller_main):
        self.__astronautas_selecionados = dict()
        self.__tarefa_selecionada = None
        self.__aevsDAO = AEVDAO()
        self.__vazao_o2 = 0.68
        self.__view_aev = ViewAEV(self)
        self.__controller_main = controller_main
        # Vazão de oxigenio em L/m baseado em:
        # https://blogs.esa.int/astronauts/2012/02/18/learning-to-spacewalk/
        # Paragrafo 5

    @property
    def aevsDAO(self):
        return self.__aevsDAO

    @property
    def aevs(self):
        return self.__aevsDAO.pega_tudo()

    @property
    def view_aev(self):
        return self.__view_aev

    @property
    def controller_main(self):
        return self.__controller_main

    @property
    def astronautas_selecionados(self):
        return self.__astronautas_selecionados

    @astronautas_selecionados.setter
    def astronautas_selecionados(self, astronautas_selecionados):
        self.__astronautas_selecionados = astronautas_selecionados

    @property
    def tarefa_selecionada(self):
        return self.__tarefa_selecionada

    @tarefa_selecionada.setter
    def tarefa_selecionada(self, tarefa):
        self.__tarefa_selecionada = tarefa

    @property
    def vazao_o2(self):
        return self.__vazao_o2

    def requisitos_missao(self):
        tipo_traje = (self.controller_main.
                      controller_traje.
                      tipo_traje.
                      Extraveicular.name)

        duracao = self.tarefa_selecionada.duracao

        capacidade_o2_necessaria = (float(duracao)*self.vazao_o2)

        return tipo_traje, capacidade_o2_necessaria

    def selecionar_astronautas(self):
        astronautas = (self.controller_main.
                       controller_astronauta.lista_obj_para_dict())
        while True:
            valores = (self.view_aev.view_selecionar_astronautas(astronautas))
            if valores is not None:
                break
        if valores == "voltar":
            pass
        else:
            codigo_astronauta_1 = int(valores["codigo_1"])
            codigo_astronauta_2 = int(valores["codigo_2"])

            astronauta1 = (self.controller_main.
                           controller_astronauta.
                           pega_astronauta_pelo_codigo(codigo_astronauta_1))
            astronauta2 = (self.controller_main.
                           controller_astronauta.
                           pega_astronauta_pelo_codigo(codigo_astronauta_2))

            tipo_traje, capacidade_o2_necessaria = self.requisitos_missao()
            astros_selecionados = {codigo_astronauta_1: astronauta1,
                                   codigo_astronauta_2: astronauta2}

            for chave, astronauta in astros_selecionados.items():
                if astronauta.traje.capacidade_o2 < capacidade_o2_necessaria:
                    raise RequisitoExcepiton((astronauta.nome,
                                              "de possuir um traje com " +
                                              "capacidade oxigenio adequado " +
                                              "para a tarefa"))
                elif astronauta.traje.tipo.name != tipo_traje:
                    raise RequisitoExcepiton(astronauta.nome,
                                             " de possuir um traje de" +
                                             "tipo Extraveicular")

            self.astronautas_selecionados = astros_selecionados

    def selecionar_tarefa(self):
        tarefas = (self.controller_main.
                   controller_tarefa.lista_obj_para_dict())
        while True:
            valores = (self.view_aev.view_selecionar_tarefa(tarefas))
            if valores is not None:
                break
        if valores == "voltar":
            pass
        else:
            codigo_tarefa = int(valores["codigo"])
            self.tarefa_selecionada = (self.controller_main.
                                       controller_tarefa.
                                       pega_tarefa_pelo_codigo(
                                           codigo_tarefa))

    def iniciar_aev(self):
        while True:
            codigo_aev = self.view_aev.view_codigos("AEV", "Inicializar")
            if self.aevsDAO.pega(codigo_aev) is None:
                break
            else:
                self.view_aev.pop_mensagem("Codigo de AEV já existe")

        aev = AEV(codigo_aev,
                  self.astronautas_selecionados,
                  self.tarefa_selecionada)
        anomalia = self.view_aev.view_aev_andamento()
        if anomalia is not None:
            aev.anomalia = anomalia
        self.aevsDAO.adiciona(aev)
        self.view_aev.pop_mensagem("Sucesso", "AEV Finalizado")

    def teste(self):
        for i in self.aevs:
            print(i.codigo)

    def relatar_anomalia(self):
        horario, tipo, descricao = (self.view_aev.
                                    view_relatar_anomalia(
                                        self.tarefa_selecionada))
        return horario, tipo, descricao

    def existe_obj(self):
        try:
            if len(self.aevs) == 0:
                raise ListaVaziaException("AEV")
        except ListaVaziaException as e:
            self.view_traje.pop_mensagem("Erro", e)
        else:
            return True

    def gerar_relatorio(self, indice):
        aev = self.aevsDAO.pega(indice)
        relatorio = Relatorio(aev)
        relatorio.gerar_relatorio()

    def pega_aev_pelo_codigo(self, codigo):
        for aev in self.aevs:
            if aev.codigo == codigo:
                return aev
        return None

    def lista_obj_para_dict(self):
        dict = {}
        for aev in self.aevs:
            dict[aev.codigo] = f"{aev.codigo};{aev.tarefa.titulo}"
        return dict

    def obj_para_dict(self, tipo: str):
        dict = {}
        if tipo == "tarefa":
            try:
                tarefa = self.tarefa_selecionada
                dict[tarefa.codigo] = f"{tarefa.titulo}"
            except AttributeError:
                return None
        elif tipo == "astronauta":
            try:
                astronautas = self.astronautas_selecionados
                for k, v in astronautas.items():
                    dict[k] = f"{v.nome}"
            except AttributeError:
                return None
        return dict

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        if (len(self.controller_main.controller_astronauta.astronautas) == 0
                and len(self.controller_main.controller_tarefa.tarefas) == 0):
            raise ListaVaziaException("Astronauta e Tarefa")
        elif len(self.controller_main.controller_astronauta.astronautas) == 0:
            raise ListaVaziaException("Astronauta")
        elif len(self.controller_main.controller_tarefa.tarefas) == 0:
            raise ListaVaziaException("Tarefa")
        else:
            switcher = {0: self.retornar,
                        1: self.iniciar_aev,
                        2: self.selecionar_astronautas,
                        3: self.selecionar_tarefa,
                        4: self.menu_opcoes,
                        7: self.teste}

            while True:
                try:
                    opcao_escolhida = self.view_aev.abrir()
                    funcao_escolhida = switcher[opcao_escolhida]
                    funcao_escolhida()
                except ObjetoDuplicadoException as e:
                    self.view_aev.pop_mensagem("Erro", e)
                except ListaVaziaException as e:
                    self.view_aev.pop_mensagem("Erro", e)
                except RequisitoExcepiton as e:
                    self.view_aev.pop_mensagem("Erro", e)
