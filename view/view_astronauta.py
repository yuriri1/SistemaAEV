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

    def dict_para_vetor(self, dicionario: dict, tipo: str):
        vetor = []
        if tipo == "matriz":
            for chave, valor in dicionario.items():
                valor = valor.split(";")
                vetor.append([chave, valor[0], valor[1], valor[2]])
        elif tipo == "lista":
            for chave, valor in dicionario.items():
                valor = valor.split(";")
                vetor.append(f"{chave} - {valor[0]} - {valor[1]}")
        return vetor

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        astronautas = self.dict_para_vetor(
            self.controller_astronauta.lista_obj_para_dict(),
            "matriz")

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
                      max_col_width=40,
                      justification='center',
                      auto_size_columns=True,
                      vertical_scroll_only=False,
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

        self.__janela = sg.Window("SCAEV - Astronautas",
                                  layout, size=self.size())

    def view_incluir(self, traje: dict):

        trajes = self.dict_para_vetor(traje, "lista")

        layout = [
            [sg.Text("Inserir Astronauta",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text("Código:",
                     font=("Gulim", 14, "bold")),
             sg.Spin([x+1 for x in range(100)], 1,
                     key="codigo",
                     font=("Gulim", 20))],
            [sg.Text("Nome:",
                     expand_x=True,
                     justification='left',
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="nome",
                          expand_x=True,
                          font=("Gulim", 20))],
            [sg.Text("Nacionalidade:",
                     expand_x=True,
                     justification='left',
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="nacionalidade",
                          expand_x=True,
                          font=("Gulim", 20))],
            [sg.Text("Traje:",
                     justification='left',
                     font=("Gulim", 14, "bold")),
             sg.InputOptionMenu(trajes,
                                auto_size_text=True,
                                key="traje",
                                expand_x=True)],
            [sg.Button("Inserir",
                       key="inserir",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 18, "bold"))],
            [sg.Button("↩",
                       focus=True,
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 20, "bold"))]
        ]
        self.__janela = sg.Window("SCAEV - Inserir Astronauta", layout)
        evento, valores = self.__janela.Read()

        if evento in (None, "voltar"):
            self.fechar()
            return "voltar"
        elif evento == "inserir":
            if (valores["nome"] == "" or valores["nacionalidade"] == "" or
                    valores["traje"] == ""):
                self.pop_mensagem("Erro", "Preencha todos os campos")
                self.fechar()
            else:
                codigo = valores["codigo"]
                nome = valores["nome"]
                nacionalidade = valores["nacionalidade"]
                traje = valores["traje"][0]
                self.fechar()

                return {"codigo": codigo,
                        "nome": nome,
                        "nacionalidade": nacionalidade,
                        "traje": traje}

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
            [sg.Button("Confirmar",
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

        self.__janela = sg.Window(("SCAEV -") +
                                  (f"{acao.capitalize()} {obj.capitalize()}"),
                                  layout)
        evento, valores = self.__janela.Read()

        if evento in (None, "voltar"):
            self.fechar()
            return None
        elif evento == "submit":
            self.fechar()
            return valores["codigo"]

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
