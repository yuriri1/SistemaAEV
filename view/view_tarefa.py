from view.abstract_view import AbstractView
import PySimpleGUI as sg


class ViewTarefa(AbstractView):
    def __init__(self, controller_tarefa):
        self.__controller_tarefa = controller_tarefa
        self.__cabecalho = ["CODIGO", "TITULO", "CAIXA", "DURAÇAO"]
        self.__janela = None
        self.iniciar_componentes()

    @property
    def controller_tarefa(self):
        return self.__controller_tarefa

    @property
    def tarefas(self):
        return self.__tarefas

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
                vetor.append(f"{chave} - {valor[0]}")

        return vetor

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        tarefas = self.dict_para_vetor(
            self.controller_tarefa.lista_obj_para_dict(), "matriz")

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
            [sg.Text("_"*80)],
            [sg.Text("Lista de Tarefas",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Table(values=tarefas,
                      key="tab_tarefas",
                      enable_events=True,
                      tooltip="Ver descrição",
                      headings=self.cabecalho,
                      max_col_width=30,
                      vertical_scroll_only=False,
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

    def view_incluir(self, caixa: dict):

        caixas = self.dict_para_vetor(caixa, "lista")

        layout = [
            [sg.Text("Inserir Tarefa",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text("Código:",
                     font=("Gulim", 14, "bold")),
             sg.Spin([x+1 for x in range(100)], 1,
                     key="codigo",
                     font=("Gulim", 20))],
            [sg.Text("Título:",
                     expand_x=True,
                     justification='left',
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="titulo",
                          expand_x=True,
                          font=("Gulim", 20))],
            [sg.Text("Duração:",
                     expand_x=True,
                     justification='left',
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="duracao",
                          expand_x=True,
                          font=("Gulim", 20))],
            [sg.Text("Caixa:",
                     justification='left',
                     font=("Gulim", 14, "bold")),
             sg.InputOptionMenu(caixas,
                                auto_size_text=True,
                                key="caixa",
                                expand_x=True)],
            [sg.Text("Descrição:",
                     justification='left',
                     expand_x=True,
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.Multiline(key="descricao",
                          expand_x=True,
                          size=(40, 6),
                          font=("Gulim", 20))],
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
            if (valores["titulo"] == "" or valores["descricao"] == "" or
                    valores["caixa"] == "" or valores["duracao"] == ""):
                self.pop_mensagem("Erro", "Preencha todos os campos")
                self.fechar()
            else:
                codigo = valores["codigo"]
                titulo = valores["titulo"]
                duracao = valores["duracao"]
                codigo_caixa = valores["caixa"][0]
                descricao = valores["descricao"]
                self.fechar()

                return {"codigo": codigo,
                        "titulo": titulo,
                        "duracao": duracao,
                        "caixa": codigo_caixa,
                        "descricao": descricao}

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

    def view_descricao_tarefa(self, valores: dict):
        tarefas_array = []
        tarefas_dict = self.controller_tarefa.lista_obj_para_dict()
        for tarefa in tarefas_dict.values():
            tarefas_array.append(tarefa)
        linha_selecionada = valores["tab_tarefas"][0]
        descricao = tarefas_array[linha_selecionada]
        descricao = descricao.split(";")
        return descricao[3]

    def abrir(self):
        self.iniciar_componentes()
        evento, valores = self.__janela.Read()

        switcher = {"inserir": 1,
                    "remover": 2}

        if evento in (None, "voltar"):
            self.fechar()
            return 0
        if evento == "tab_tarefas":
            self.pop_mensagem("Descrição da Tarefa",
                              self.view_descricao_tarefa(valores))
            self.fechar()
            return 3

        else:
            self.fechar()
            return switcher[evento]

    def fechar(self):
        self.__janela.Close()

    def pop_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
