import PySimpleGUI as sg
from view.abstract_view import AbstractView


class ViewAstronauta(AbstractView):
    def __init__(self, controller_astronauta):
        self.__controller_astronauta = controller_astronauta
        self.__cabecalho = ["CODIGO", "NOME", "NACIONALIDADE", "TRAJE"]
        self.__janela = None
        self.iniciar_componentes()

    @property
    def controller_astronauta(self):
        return self.__controller_astronauta

    @property
    def cabecalho(self):
        return self.__cabecalho

    def dict_para_matriz(self, dicionario: dict):
        matriz = []
        for chave, valor in dicionario.items():
            valor.split(";")
            matriz.append([chave, valor[0], valor[1], valor[2]])
        return matriz

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        astronautas = self.dict_para_matriz(
            self.controller_astronauta.lista_obj_para_dict())

        layout = [
            [sg.Text("Menu de Astronautas",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Button("INSERIR",
                       key="inserir",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Button("REMOVER",
                       key="remover",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Text("_"*80)],
            [sg.Text("Lista de Astronautas",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Table(values=astronautas,
                      headings=self.cabecalho,
                      justification='center',
                      auto_size_columns=True,
                      expand_x=True,
                      size=(0, 20),
                      font=("Gulim", 14, "bold"))],
            [sg.Button("???",
                       focus=True,
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 23, "bold"))]
        ]

        self.__janela = sg.Window("SCAEV - Astronautas",
                                  layout, size=self.size())

    def abrir(self):
        self.iniciar_componentes()
        evento, valores = self.__janela.Read()

        switcher = {"inserir": 1,
                    "remover": 2}

        if evento in (None, "voltar"):
            self.fechar()
            return 0

        self.fechar()
        return switcher[evento]

    def fechar(self):
        self.__janela.Close()

    def pop_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
