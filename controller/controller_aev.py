from model.aev import AEV
from view.view_aev import ViewAEV
from controller.abstract_controller import AbstractController
from relatorios.relatorio import Relatorio
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException
from exception.requisito_exception import RequisitoExcepiton


class ControllerAEV(AbstractController):
    def __init__(self, controller_main):
        self.__aevs = []
        self.__view_aev = ViewAEV()
        self.__controller_main = controller_main
        self.__astronautas_selecionados = []
        self.__tarefa_selecionada = None
        self.__vazao_o2 = 0.68
        # Vazão de oxigenio em L/m baseado em:
        # https://blogs.esa.int/astronauts/2012/02/18/learning-to-spacewalk/
        # Paragrafo 5

    @property
    def aevs(self):
        return self.__aevs

    @property
    def view_aev(self):
        return self.__view_aev

    @property
    def controller_main(self):
        return self.__controller_main

    @property
    def astronautas_selecionados(self):
        return self.__astronautas_selecionados

    @property
    def tarefa_selecionada(self):
        return self.__tarefa_selecionada

    @tarefa_selecionada.setter
    def tarefa_selecionada(self, tarefa):
        self.__tarefa_selecionada = tarefa

    @property
    def vazao_o2(self):
        return self.__vazao_o2

    def selecionar_astronautas(self):
        if self.tarefa_selecionada is None:
            raise ListaVaziaException("Tarefa Selecionada")
        else:
            lista_astronautas = (self.
                                 controller_main.
                                 controller_astronauta.
                                 astronautas.copy())
            ctrl_astronauta = (self.
                               controller_main.
                               controller_astronauta)
            astronautas_escolhidos = (self.
                                      view_aev.
                                      view_selecionar_astronauta(
                                          lista_astronautas,
                                          ctrl_astronauta))
            extraveicular = (self.controller_main.
                             controller_traje.
                             tipo_traje.
                             Extraveicular.name)
            duracao = self.tarefa_selecionada.duracao

            capacidade_o2_necessaria = (duracao*self.vazao_o2)

            for astronauta in astronautas_escolhidos:
                if astronauta.traje.tipo.name != extraveicular:
                    self.tarefa_selecionada = None
                    raise RequisitoExcepiton("Possuir um traje Extraveicular")
                elif (astronauta.traje.capacidade_o2 <
                      capacidade_o2_necessaria):
                    self.tarefa_selecionada = None
                    raise RequisitoExcepiton("Possuir um traje com capacidade\
oxigenio adequado para a tarefa")
                else:
                    (self.astronautas_selecionados.
                     append(astronautas_escolhidos))
                    self.view_aev.view_mensagem('''Astronauta(s) selecionados
com sucesso!''')

    def selecionar_tarefa(self):
        lista_tarefas = (self.
                         controller_main.
                         controller_tarefa.
                         tarefas.copy())
        ctrl_tarefas = (self.controller_main.controller_tarefa)
        tarefas_selecionadas = (self.view_aev.
                                view_selecionar_tarefa(
                                    lista_tarefas, ctrl_tarefas))
        self.tarefa_selecionada = tarefas_selecionadas

    def iniciar_aev(self):
        if self.tarefa_selecionada is None:
            raise ListaVaziaException("Tarefa selecionada")
        elif len(self.astronautas_selecionados) == 0:
            raise ListaVaziaException("Astronauta selecionado")
        elif (self.tarefa_selecionada is None
              and len(self.astronautas_selecionados) == 0):
            raise ListaVaziaException("Astronauta e Tarefa selecionados")
        else:
            codigos = []
            codigo = self.view_aev.view_codigos(None, "da AEV: ")
            anomalia = None
            for i in self.aevs:
                codigos.append(i.codigo)
            if (codigo not in codigos):
                aev = AEV(codigo, self.astronautas_selecionados,
                          self.tarefa_selecionada)
                while True:
                    opcao = self.view_aev.view_aev_andamento(codigo)
                    if opcao == 1:
                        self.aevs.append(aev)
                        break
                    elif opcao == 2:
                        anomalia = self.view_aev.view_relatar_anomalia(
                            self.tarefa_selecionada)
                        aev.anomalia = (anomalia)
                self.view_aev.view_mensagem("AEV encerrada com sucesso")
            else:
                raise ObjetoDuplicadoException("um AEV")

    def relatar_anomalia(self):
        horario, tipo, descricao = (self.view_aev.
                                    view_relatar_anomalia(
                                        self.tarefa_selecionada))
        return horario, tipo, descricao

    def listar(self):
        try:
            if len(self.aevs) == 0:
                raise ListaVaziaException("AEV")
        except ListaVaziaException as e:
            self.view_traje.pop_mensagem("Erro", e)
        else:
            self.view_aev.view_listar(self.aevs)
            return True

    def gerar_relatorio(self):
        if self.listar():
            codigos = []
            for aev in self.aevs:
                codigos.append(aev.codigo)
            aev = (self.
                   pega_aev_pelo_codigo(
                       (self.view_aev.
                        view_codigos(codigos, "AEV", "gerar o relatório: "))))
            relatorio = Relatorio(aev)
            relatorio.gerar_relatorio()

    def pega_aev_pelo_codigo(self, codigo):
        for aev in self.aevs:
            if aev.codigo == codigo:
                return aev
        return None

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
                        4: self.listar,
                        5: self.gerar_relatorio}

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
