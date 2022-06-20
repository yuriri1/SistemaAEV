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
            codigo, nome, nacionalidade, traje = (self.
                                                  view_astronauta.
                                                  view_incluir(lista_trajes,
                                                               ctrl_traje))
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
                    self.view_astronauta.view_mensagem("Inserido com sucesso")
                else:
                    raise ObjetoDuplicadoException("um astronauta")
            
    def excluir(self):
        if self.listar():
            codigos = []
            for astronauta in self.astronautas:
                codigos.append(astronauta.codigo)
            escolha_remocao = (self.view_astronauta.
                               view_codigos(codigos, "astronauta", "excluir"))
            astro = self.pega_astronauta_pelo_codigo(escolha_remocao)
            astro.traje.dono = None
            self.astronautas.remove(astro)
            self.view_astronauta.view_mensagem("Excluido com sucesso!")

    def alterar(self):
        if self.listar():
            codigos = []
            for astronautas in self.astronautas:
                codigos.append(astronautas.codigo)
            escolha_edicao = self.view_astronauta.view_codigos(codigos,
                                                               "astronauta",
                                                               "editar")
            for astronautas in self.astronautas:
                if escolha_edicao == astronautas.codigo:
                    nome, nacionalidade = self.view_astronauta.view_editar()

    
    def listar(self):
        try:
            if len(self.astronautas) == 0:
                raise ListaVaziaException("Astronauta")
        except ListaVaziaException as e:
            print(e)
        else:
            self.view_astronauta.view_listar(self.astronautas)
            return True

    def pega_astronauta_pelo_codigo(self, codigo: list):
        for astronauta in self.astronautas:
            if astronauta.codigo == codigo:
                return astronauta
        return None


    def retornar(self):
        self.__manter_tela = False
    
    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir, 
                    2: self.excluir, 3: self.alterar, 
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