from view.abstract_view import AbstractView
import PySimpleGUI as sg


class ViewTraje(AbstractView):
    def __init__(self, controller_traje):
        self.__controller_traje = controller_traje
        self.__cabecalho = ["CODIGO", "TIPO", "CAP. O2 (L)", "DONO"]
        self.__janela = None
        self.iniciar_componentes()

    @property
    def controller_traje(self):
        return self.__controller_traje

    @property
    def cabecalho(self):
        return self.__cabecalho

    def dict_para_matriz(self, dicionario: dict):
        matriz = []
        for chave, valor in dicionario.items():
            valor = valor.split(";")
            matriz.append([chave, valor[0], valor[1], valor[2]])

        return matriz

    def str_para_tupla(self, string: str):
        return tuple(string.split(";"))

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        trajes = self.dict_para_matriz(
            self.controller_traje.lista_obj_para_dict())

        layout = [
            [sg.Text("Menu de Trajes",
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
            [sg.Text("Lista de Trajes",
                     font=("Gulim", 18))],
            [sg.Table(values=trajes,
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

        self.__janela = sg.Window("SCAEV - Trajes", layout, size=self.size())

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

    def view_incluir(self, tipos: str):
        layout = [
            [sg.Text("Inserir Traje",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text("Código:", font=("Gulim", 14, "bold")),
             sg.Spin([x+1 for x in range(100)], 1,
                     key="codigo",
                     expand_x=True,
                     font=("Gulim", 20))],
            [sg.Text("Tipo:",
                     expand_x=True,
                     font=("Gulim", 14, "bold")),
             sg.InputOptionMenu(self.str_para_tupla(tipos),
                                auto_size_text=True,
                                key="tipo",
                                expand_x=True)],
            [sg.Text("Capacidade O2 (L):",
                     expand_x=True,
                     font=("Gulim", 14, "bold")),
             sg.Slider(range=(0, 500),
                       expand_x=True,
                       orientation='h',
                       default_value=0, key="cap")],
            [sg.Button("Inserir",
                       key="inserir",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 18, "bold")),
             sg.Button("↩",
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 20, "bold"))]
        ]
        self.__janela = sg.Window("SCAEV - Inserir Traje",
                                  layout)
        evento, valores = self.__janela.Read()

        if evento in (None, "voltar"):
            self.fechar()
            return "voltar"
        elif evento == "inserir":
            if (valores["tipo"] == "" or valores["cap"] == 0):
                self.pop_mensagem("Erro", "Campos não podem estar vazio")
                self.fechar()
            else:
                codigo = valores["codigo"]
                tipo = valores["tipo"]
                capacidade = valores["cap"]
                self.fechar()

                return {"codigo": codigo,
                        "tipo": tipo,
                        "capacidade": capacidade}

    def view_codigos(self, obj: str, acao: str):
        layout = [
            [sg.Text(f"{acao.capitalize()} {obj.capitalize()}",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text(f"Código do(a) {obj.capitalize()} que deseja {acao}:",
                     justification='center',
                     font=("Gulim", 14)),
             sg.Spin([x+1 for x in range(100)], 1,
                     key="codigo",
                     font=("Gulim", 20))],
            [sg.Button("Submeter",
                       key="submit",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 18, "bold")),
             sg.Button("↩",
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 20, "bold"))]
        ]

        self.__janela = sg.Window(f"SCAEV -\
{acao.capitalize()} {obj.capitalize()}", layout)
        evento, valores = self.__janela.Read()

        if evento in (None, "voltar"):
            self.fechar()
            return None
        elif evento == "submit":
            self.fechar()
            return valores["codigo"]

    def fechar(self):
        self.__janela.Close()

    def pop_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
