import PySimpleGUI as sg
from view.abstract_view import AbstractView


class ViewFerramenta(AbstractView):
    def __init__(self, controller_ferramenta):
        self.__controller_ferramenta = controller_ferramenta
        self.__cabecalho = ["ID", "Nome"]
        self.__janela = None
        self.iniciar_componentes()

    @property
    def controller_ferramenta(self):
        return self.__controller_ferramenta

    @property
    def cabecalho(self):
        return self.__cabecalho

    def view_incluir(self):
        pass

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        ferramentas = self.dict_para_matriz(
            self.controller_ferramenta.lista_obj_para_dict())

        layout = [
            [sg.Text("Menu de Ferramentas",
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
            [sg.Button("EDITRAR",
                       key="editar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Text("_"*80)],
            [sg.Text("Lista de Ferramentas",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Table(values=ferramentas,
                      headings=self.cabecalho,
                      justification='center',
                      auto_size_columns=True,
                      expand_x=True,
                      size=(0, 20),
                      font=("Gulim", 14, "bold"))],
            [sg.Button("↩",
                       focus=True,
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 23, "bold"))]
        ]

        self.__janela = sg.Window("SCAEV - Ferramentas",
                                  layout, size=self.size())

    def abrir(self):
        self.iniciar_componentes()
        evento, valores = self.__janela.Read()

        switcher = {"inserir": 1,
                    "remover": 2,
                    "editar": 3}

        if evento in (None, "voltar"):
            self.fechar()
            return 0

        self.fechar()
        return switcher[evento]

    def fechar(self):
        self.__janela.Close()

    def pop_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
