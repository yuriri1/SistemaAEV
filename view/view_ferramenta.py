import PySimpleGUI as sg
from view.abstract_view import AbstractView


class ViewFerramenta(AbstractView):
    def __init__(self, controller_ferramenta):
        self.__controller_ferramenta = controller_ferramenta
        self.__cabecalho = ["CODIGO", "NOME"]
        self.__janela = None
        self.iniciar_componentes()

    @property
    def controller_ferramenta(self):
        return self.__controller_ferramenta

    @property
    def cabecalho(self):
        return self.__cabecalho

    def num_codigos(self):
        numeros = set()

        for i in range(1, 100):
            numeros.add(str(i))

        return numeros

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
                      header_relief='flat',
                      vertical_scroll_only=False,
                      font=("Gulim", 16, "bold"))],
            [sg.Button("↩",
                       focus=True,
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 23, "bold"))]
        ]

        self.__janela = sg.Window("SCAEV - Ferramentas",
                                  layout, size=self.size())

    def view_incluir(self):
        layout = [
            [sg.Text("Inserir Ferramenta",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text("Código:",
                     justification='center',
                     font=("Gulim", 14, "bold")),
             sg.Spin([x+1 for x in range(100)], 1,
                     key="codigo",
                     font=("Gulim", 20))],
            [sg.Text("Nome:",
                     justification='center',
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="nome", font=("Gulim", 20))],
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
        self.__janela = sg.Window("SCAEV - Inserir Ferramenta",
                                  layout)
        evento, valores = self.__janela.Read()

        if evento in (None, "voltar"):
            self.fechar()
            return "voltar"
        elif evento == "inserir":
            if (valores["nome"] == ""):
                self.pop_mensagem("Erro", "Campo 'Nome' não pode estar vazio")
                self.fechar()
            else:
                codigo = valores["codigo"]
                nome = valores["nome"]
                self.fechar()

                return {'codigo': codigo, 'nome': nome}

    def view_editar(self):
        layout = [
            [sg.Text("Editar Ferramenta",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text("Nome:",
                     justification='center',
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="nome", font=("Gulim", 20))],
            [sg.Button("Editar",
                       key="editar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 18, "bold")),
             sg.Button("↩",
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 20, "bold"))]
        ]
        self.__janela = sg.Window("SCAEV - Editar Ferramenta",
                                  layout)
        evento, valores = self.__janela.Read()
        if evento in (None, "voltar"):
            self.fechar()
            return 'voltar'
        elif evento == "editar":
            if (valores["nome"] == ""):
                self.pop_mensagem("Erro", "Campo 'Nome' não pode estar vazio")
                self.fechar()
            else:
                self.fechar()
                return valores["nome"]

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
            return 'voltar'
        elif evento == "submit":
            self.fechar()
            return valores["codigo"]

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
