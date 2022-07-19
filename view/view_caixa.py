from view.abstract_view import AbstractView
import PySimpleGUI as sg


class ViewCaixa(AbstractView):
    def __init__(self, controller_caixa):
        self.__controller_caixa = controller_caixa
        self._cabecalho = ["CODIGO", "NOME", "FERRAMENTAS"]
        self.__janela = None
        self.iniciar_componentes()

    @property
    def controller_caixa(self):
        return self.__controller_caixa

    @property
    def cabecalho(self):
        return self._cabecalho

    def dict_para_matriz(self, dicionario: dict):
        matriz = []
        for chave, valor in dicionario.items():
            valor.split(";")
            matriz.append([chave, valor[0], valor[1]])
        return matriz

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        caixas = self.dict_para_matriz(
            self.controller_caixa.lista_obj_para_dict())

        layout = [
            [sg.Text("Menu de Caixa de Ferramentas",
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
            [sg.Text("Lista de Caixa de Ferramentas",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Table(values=caixas,
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

        self.__janela = sg.Window("SCAEV - Caixa de Ferramentas",
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
