import re
from view.abstract_view import AbstractView

class ViewAstronauta(AbstractView):
    def __init__(self):
        pass
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DO ASTRONAUTA")
        print("1 - Inserir Astronauta")
        print("2 - Remover Astronauta")
        print("3 - Editar Astronauta")
        print("4 - Listar Astronauta")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ",[0, 1, 2, 3, 4])
        return opcao
    
    def __view_trajes_disponiveis(self, trajes: list):
        print("-"*50)
        print(f"{'TRAJES DISPONIVEIS': ^40}")
        print(f"{'CODIGO': <10}{'TIPO': ^20}{'CAPACIDADE 02': >15}")
        for traje in trajes:
            if traje.dono is None:
                print(f"{traje.codigo: <10}{traje.tipo.name: ^20}\
{traje.capacidade_o2: >15}")
        print("-"*50)
        
    def view_incluir(self, trajes: list, c_traje: object):
        print("MENU INICIAL ---> MENU DO ASTRONAUTA\
--> INCLUIR ASTRONAUTA")
        codigo = self.le_num_inteiro("Codigo do astronauta: ")
        nome = str(input("Nome do astronauta: ")).capitalize()
        nacionalidade = str(input("Nacionalidade do astronauta: "))
        self.__view_trajes_disponiveis(trajes)
        codigos = []
        for j in trajes:
            codigos.append(j.codigo)
        codigo_selecionado = (self.
                              le_num_inteiro("Digite o codigo do traje: ",
                                             codigos))
        traje_escolhido = (c_traje.
                           pega_traje_pelo_codigo(codigo_selecionado))
            
        return codigo, nome, nacionalidade, traje_escolhido
        
    def view_listar(self, astronautas: list):
        print("-"*70)
        print(f"{'CODIGO': <10}{'NOME': ^15}{'NACIONALIDADE': ^15}\
{'TRAJE': >15}")
        for astronauta in astronautas:
            print(f"{astronauta.codigo: <10}{astronauta.nome: ^15}\
{astronauta.nacionalidade: ^15}{astronauta.traje.tipo.name: >15}")
        print("-"*70)
        
        
    def view_editar(self):
        nome = str(input("Escreva o nome: ")).capitalize()
        nacionalidade = str(input("Escreva a nacionalidade: ")).capitalize()
        return nome, nacionalidade