from view.abstract_view import AbstractView
import PySimpleGUI as sg


class ViewAEV(AbstractView):
    def __init__(self):
        self.__janela = None
        self.iniciar_componentes()

    def view_incluir(self):
        pass

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        layout = [
            [sg.Text("Menu de AEV's",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Button("INICIAR AEV",
                       disabled=True,
                       key="iniciar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Button("SELECIONAR ASTRONAUTA",
                       disabled=True,
                       key="selec_astro",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Button("SELECIONAR TAREFA",
                       disabled=True,
                       key="selec_tarefa",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Text("_"*50)],
            [sg.Text("Lista de AEV's",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 15))],
            [sg.Text("Selecione um aev para gerar um relatório",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 15))],
            [sg.Listbox([],
                        expand_x=True,
                        size=(0, 15),
                        font=("Gulim", 14, "bold"),
                        enable_events=True)],
            [sg.Button("↩",
                       focus=True,
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 23, "bold"))]
        ]

        self.__janela = sg.Window("SCAEV - AEV",
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
