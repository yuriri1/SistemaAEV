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

    def dict_para_vetor(self, dicionario: dict, tipo: str):
        vetor = []
        if tipo == "matriz":
            for chave, valor in dicionario.items():
                valor = valor.split(";")
                vetor.append([chave, valor[0], valor[1]])
        elif tipo == "lista":
            for chave, valor in dicionario.items():
                vetor.append(f"{chave} - {valor}")

        return vetor

    def tamanho_coluna(self, matriz: list):
        maior = 0
        for linha in matriz:
            if len(linha[2]) > maior:
                maior = len(linha[2])
        return maior

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        caixas = self.dict_para_vetor(
            self.controller_caixa.lista_obj_para_dict(),
            "matriz")

        tam_coluna = self.tamanho_coluna(caixas)

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
                      max_col_width=tam_coluna + 10,
                      headings=self.cabecalho,
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

        self.__janela = sg.Window("SCAEV - Caixa de Ferramentas",
                                  layout, size=self.size())

    def view_incluir(self, ferramenta: dict):

        ferramentas = self.dict_para_vetor(
            ferramenta,
            "lista")

        layout = [
            [sg.Text("Inserir Caixa de Ferramentas",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text("Código:",
                     justification='left',
                     font=("Gulim", 14, "bold")),
             sg.Spin([x+1 for x in range(100)], 1,
                     key="codigo",
                     font=("Gulim", 20))],
            [sg.Text("Nome:",
                     justification='left',
                     expand_x=True,
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="nome",
                          expand_x=True,
                          font=("Gulim", 20))],
            [sg.Text("Selecione a(s) ferramenta(s):",
                     justification='left',
                     font=("Gulim", 14, "bold")),
             sg.Listbox(ferramentas,
                        select_mode="extended",
                        key="ferramentas",
                        size=(0, 5),
                        auto_size_text=True,
                        font=("Gulim", 20))],
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

        self.__janela = sg.Window("SCAEV - Inserir Caixa", layout)
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
                lista_ferramentas = valores["ferramentas"]
                ferramentas = []
                for ferramenta in lista_ferramentas:
                    ferramentas.append(ferramenta[0])
                self.fechar()

                return {'codigo': codigo,
                        'nome': nome,
                        'ferramentas': ferramentas}

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
