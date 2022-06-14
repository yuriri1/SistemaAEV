from model.ferramenta import Ferramenta
from view.view_ferramenta import ViewFerramenta

class ControllerFerramenta:
    def __init__(self):
        self.__ferramentas = []
        self.__view_ferramenta = ViewFerramenta()

    def incluir(self):
        print("INCLUIR")

    def alterar(self):
        print("ALTERAR")

    def excluir(self):
        print("EXCLUIR")

    def listar(self):
        print("LISTAR")

    def retornar(self):
        self.__manter_tela = False
    
    def menu_opcoes(self):
        switcher = {0: self.retornar, 1: self.incluir, 
                    2: self.alterar, 3: self.excluir, 
                    4: self.listar}
        
        self.__manter_tela = True
        
        while self.__manter_tela:
            opcao_escolhida = self.__view_ferramenta.view_opcoes()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()