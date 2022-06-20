from cmath import e
import re
from typing import List
from model.tarefa import Tarefa
from view.view_tarefa import ViewTarefa
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException

class ControllerTarefa:
    def __init__(self,controller_main):
        self.__tarefas = []
        self.__view_tarefa = ViewTarefa()
        self.__controller_main = controller_main
        self.__manter_tela = True
        
    @property
    def tarefas(self):
        return self.__tarefas
    
    @property
    def view_tarefa(self):
        return self.__view_tarefa
    
    @property
    def controller_main(self):
        return self.__controller_main
        
    def incluir(self):
        lista_caixas = (self.
                        controller_main.
                        controller_caixa.
                        caixas.copy())
        ctrl_caixa = self.controller_main.controller_caixa
        if len(lista_caixas) == 0:
            raise ListaVaziaException("Caixa")
        else:
            codigos = []
            codigo, titulo, descricao, duracao, caixa = (self.
                                                         view_tarefa.
                                                         view_incluir(
                                                             lista_caixas,
                                                             ctrl_caixa))
            
            tarefa = Tarefa(codigo, titulo, descricao, caixa, duracao)
            if len(self.tarefas) == 0:
                self.tarefas.append(tarefa)
                self.view_tarefa.view_mensagem("Inserido com sucesso!")
            else:
                for t in self.tarefas:
                    codigos.append(t.codigo)
                if codigo not in codigos:
                    self.tarefas.append(tarefa)
                    self.view_tarefa.view_mensagem("Inserido com sucesso!")
                else:
                    raise ObjetoDuplicadoException("uma tarefa")
    
    def excluir(self):
        if self.listar():
            codigos = []
            for tarefa in self.tarefas:
                codigos.append(tarefa.codigo)
            escolha_remocao = (self.view_tarefa.
                               view_codigos(codigos, "tarefa", "excluir"))
            self.tarefas.remove(self.pega_tarefa_pelo_codigo(escolha_remocao))
            self.view_caixa.view_mensagem("Excluido com sucesso!")

    
    def listar(self):
        try:
            if len(self.tarefas) == 0:
                raise ListaVaziaException("Tarefa")
        except ListaVaziaException as e:
            print(e)
        else:          
            self.view_tarefa.view_listar(self.tarefas)
            return True

    def retornar(self):
        self.__manter_tela = False
        
    def pega_tarefa_pelo_codigo(self, codigo: int):
        for tarefa in self.tarefas:
            if tarefa == codigo:
                return tarefa
        return None
    
    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir, 
                    2: self.excluir, 3: self.listar}
        
        self.__manter_tela = True
        
        while self.__manter_tela:
            try:
                opcao_escolhida = self.__view_tarefa.view_opcoes()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                print(e)
            except ListaVaziaException as e:
                print(e)