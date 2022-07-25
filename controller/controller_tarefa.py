from model.tarefa import Tarefa
from persistence.tarefaDAO import TarefaDAO
from view.view_tarefa import ViewTarefa
from controller.abstract_controller import AbstractController
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException


class ControllerTarefa(AbstractController):
    def __init__(self, controller_main):
        self.__tarefasDAO = TarefaDAO()
        self.__view_tarefa = ViewTarefa(self)
        self.__controller_main = controller_main

    @property
    def tarefasDAO(self):
        return self.__tarefasDAO

    @property
    def tarefas(self):
        return self.__tarefasDAO.pega_tudo()

    @property
    def view_tarefa(self):
        return self.__view_tarefa

    @property
    def controller_main(self):
        return self.__controller_main

    def incluir(self):
        if len(self.controller_main.controller_caixa.caixas) == 0:
            raise ListaVaziaException("Caixa")
        else:
            caixas = (self.controller_main.
                      controller_caixa.lista_obj_para_dict())
            while True:
                valores = self.view_tarefa.view_incluir(caixas)
                if valores is not None:
                    break
            if valores == "voltar":
                pass
            else:
                codigo = valores["codigo"]
                titulo = valores["titulo"]
                duracao = valores["duracao"]
                descricao = valores["descricao"]
                codigo_caixa = str(valores["caixa"])
                caixa = (self.controller_main.controller_caixa.
                         pega_caixa_pelo_codigo(codigo_caixa))
                tarefa = Tarefa(codigo, titulo, descricao, caixa, duracao)
                if self.tarefasDAO.adiciona(tarefa) is None:
                    raise ObjetoDuplicadoException("uma Tarefa")
                else:
                    (self.view_tarefa.
                     pop_mensagem("✓", " Incluido com sucesso!"))

    def excluir(self):
        if self.existe_obj():
            escolha_remocao = (self.view_tarefa.
                               view_codigos("Tarefa", "excluir"))
            if escolha_remocao == "voltar":
                pass
            else:
                if (self.pega_tarefa_pelo_codigo(escolha_remocao) is not None):
                    (self.tarefasDAO.
                     remove(self.pega_tarefa_pelo_codigo(escolha_remocao)))
                    self.view_tarefa.pop_mensagem("✓",
                                                  " Excluido com sucesso!")
                else:
                    (self.view_tarefa.
                     pop_mensagem("Erro", "Tarefa não encontrada"))

    def existe_obj(self):
        try:
            if len(self.tarefas) == 0:
                raise ListaVaziaException("Tarefa")
        except ListaVaziaException as e:
            self.view_tarefa.pop_mensagem("Erro de lista vazia", e)
        else:
            return True

    def lista_obj_para_dict(self):
        dict = {}
        for tarefa in self.tarefas:
            dict[tarefa.codigo] = ((f"{tarefa.titulo};") +
                                   (f"{tarefa.caixa.nome};") +
                                   (f"{tarefa.duracao} min;") +
                                   (f"{tarefa.descricao}"))

        return dict

    def pega_tarefa_pelo_codigo(self, codigo: int):
        for tarefa in self.tarefas:
            if tarefa.codigo == codigo:
                return tarefa
        return None

    def retornar(self):
        self.controller_main.iniciar_sistema()

    def menu_opcoes(self):
        switcher = {0: self.retornar,
                    1: self.incluir,
                    2: self.excluir,
                    3: self.menu_opcoes}

        while True:
            try:
                opcao_escolhida = self.__view_tarefa.abrir()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                self.view_tarefa.pop_mensagem("Erro", e)
            except ListaVaziaException as e:
                self.view_tarefa.pop_mensagem("Erro", e)
