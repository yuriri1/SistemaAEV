from model.astronauta import Astronauta
from view.view_astronauta import ViewAstronauta
from exception.objeto_duplicado_exception import ObjetoDuplicadoException
from exception.lista_vazia_exception import ListaVaziaException

class ControllerAstronauta:
    def __init__(self,controller_main):
        self.__astronautas = []
        self.__view_astronauta = ViewAstronauta()
        self.__controller_main = controller_main
        self.__manter_tela = True
        
    @property
    def astronautas(self):
        return self.__astronautas
    
    @property
    def view_astronauta(self):
        return self.__view_astronauta
    
    @property
    def controller_main(self):
        return self.__controller_main
        
    def incluir(self):
        lista_trajes = self.controller_main.controller_traje.trajes.copy()
        ctrl_traje = self.controller_main.controller_traje
        if len(lista_trajes) == 0:
            raise ListaVaziaException("Traje")
        else:
            codigos=[]
            codigo, nome, nacionalidade, traje = self.view_astronauta.view_incluir(
                lista_trajes,
                ctrl_traje
            )
            astronauta = Astronauta(codigo, nome, nacionalidade, traje)
            if len(self.astronautas) == 0:
                self.astronautas.append(astronauta)
                traje.dono = astronauta
                self.view_astronauta.view_mensagem("Inserido com sucesso!")
            else:
                for a in self.astronautas:
                    codigos.append(a.codigo)
                if codigo not in codigos:
                    self.astronautas.append(astronauta)
                    traje.dono = astronauta
                    self.view_astronauta.view_mensagem("Inserido com sucesso!")
                else:
                    raise ObjetoDuplicadoException("um astronauta")
            
    def excluir(self):
            print("EXCLUIR")

    def alterar(self):
        print("ALTERAR")

    
    def listar(self):
        try:
            if len(self.astronautas) == 0:
                raise ListaVaziaException("Astronauta")
        except ListaVaziaException as e:
            print(e)
        else:
            self.view_astronauta.view_listar(self.astronautas)

    def retornar(self):
        self.__manter_tela = False
    
    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir, 
                    2: self.alterar, 3: self.excluir, 
                    4: self.listar}
        
        self.__manter_tela = True
        
        while self.__manter_tela:
            try:
                opcao_escolhida = self.__view_astronauta.view_opcoes()
                funcao_escolhida = switcher[opcao_escolhida]
                funcao_escolhida()
            except ObjetoDuplicadoException as e:
                print(e)
            except ListaVaziaException as e:
                print(e)