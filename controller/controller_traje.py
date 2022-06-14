from model.traje import Traje
from model.tipo_traje import TipoTraje
from view.view_traje import ViewTraje
from exception.objeto_duplicado_exception import ObjetoDuplicadoException

class ControllerTraje:
    def __init__(self):
        self.__trajes = []
        self.__view_traje = ViewTraje()
        self.__tipo_traje = TipoTraje
        
    
    @property
    def trajes(self):
        return self.__trajes
        
    def incluir(self):
            codigos = []
            codigo, tipo, capacidade_o2 = self.__view_traje \
                                            .view_incluir(self.__tipo_traje)
            traje = Traje(codigo, tipo, capacidade_o2)
            if len(self.trajes)  == 0:
                self.trajes.append(traje)   
            else:
                for t in self.trajes:
                    codigos.append(t.codigo)
                if codigo not in codigos:
                    self.trajes.append(traje)
                else:
                    raise ObjetoDuplicadoException("um com o codigo", "um traje")

    def excluir(self):
        try:
            self.listar()
            codigos = []
            for i in self.trajes:
                codigos.append(i.codigo)
            escolha_remocao = self.__view_traje.view_excluir(codigos)
            for i, j in enumerate(self.trajes):
                if escolha_remocao == j.codigo:
                    self.trajes.pop(i)
                    self.__view_traje.view_mensagem("Excluido com sucesso")
        except IndexError:
            print("Nenhum traje no sistema")

    def listar(self):
        self.__view_traje.view_listar(self.trajes)

    def retornar(self):
        self.__manter_tela = False
    
    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir, 
                    2: self.excluir, 4: self.listar}
        
        self.__manter_tela = True
        
        while self.__manter_tela:
            try:
                opcao_escolhida = self.__view_traje.view_opcoes()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                print(e)