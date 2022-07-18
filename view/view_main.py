import PySimpleGUI as sg
from view.abstract_view import AbstractView


class ViewMain(AbstractView):
    def __init__(self):
        self.__janela = None
        self.iniciar_componentes()

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        layout = [
            [sg.Text("Sistema de Controle de AEV's",
                     font=("Gulim", 18),
                     expand_x=True,
                     justification="center")],
            [sg.Button("AEV's",
                       key="iniciar_aev",
                       expand_y=True,
                       expand_x=True,
                       font=("Gulim", 16, "bold"))],
            [sg.Button("CONFIGURAR ASTRONAUTAS",
                       key="astronautas",
                       expand_y=True,
                       expand_x=True,
                       font=("Gulim", 16, "bold"))],
            [sg.Button("CONFIGURAR TAREFAS",
                       key="tarefas",
                       expand_y=True,
                       expand_x=True,
                       font=("Gulim", 16, "bold"))],
            [sg.Button("CONFIGURAR TRAJES",
                       key="trajes",
                       expand_y=True,
                       expand_x=True,
                       font=("Gulim", 16, "bold"))],
            [sg.Button("CONFIGURAR CAIXA DE FERRAMENTAS",
                       key="caixas",
                       expand_y=True,
                       expand_x=True,
                       font=("Gulim", 15, "bold"))],
            [sg.Button("CONFIGURAR FERRAMENTAS",
                       key="ferramentas",
                       expand_y=True,
                       expand_x=True,
                       font=("Gulim", 16, "bold"))],
            [sg.Button("SAIR DO SISTEMA",
                       focus=True,
                       key="sair",
                       expand_y=True,
                       expand_x=True,
                       font=("Gulim", 16, "bold"))],
        ]

        self.__janela = sg.Window("SCAEV", layout, size=self.size())

    def abrir(self):
        self.iniciar_componentes()
        evento, valores = self.__janela.Read()

        switcher = {"iniciar_aev": 1,
                    "astronautas": 2,
                    "tarefas": 3,
                    "trajes": 4,
                    "caixas": 5,
                    "ferramentas": 6}
        if evento in (None, "sair"):
            return 0
        self.fechar()
        return switcher[evento]

    def fechar(self):
        self.__janela.Close()

    def pop_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
