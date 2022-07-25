from view.abstract_view import AbstractView
import PySimpleGUI as sg


class ViewAEV(AbstractView):
    def __init__(self, controller_aev):
        self.__controller_aev = controller_aev
        self.__cabecalho = ["CODIGO", "TITULO DA TAREFA"]
        self.__janela = None
        self.iniciar_componentes()

    @property
    def controller_aev(self):
        return self.__controller_aev

    @property
    def cabecalho(self):
        return self.__cabecalho

    def dict_para_vetor(self, dicionario: dict, tipo: str):
        vetor = []
        if tipo == "matriz":
            for chave, valor in dicionario.items():
                vetor.append([chave, valor])
        elif tipo == "lista":
            for chave, valor in dicionario.items():
                valor = valor.split(";")
                vetor.append(f"{chave} - {valor[0]} - {valor[1]} - {valor[2]}")
        return vetor

    def tarefa_selecionada(self):
        if self.controller_aev.obj_para_dict("tarefa") is None:
            return "Tarefa selecionada: Nenhuma"
        for k, v in self.controller_aev.obj_para_dict("tarefa").items():
            return f"Tarefa selecionada: {k} - {v}"

    def astronauta_selecionado(self):
        if (self.controller_aev.obj_para_dict("astronauta") is None or
                self.controller_aev.obj_para_dict("astronauta") == {}):
            return "Astronauta selecionado: Nenhum"
        tooltip = "Astronautas Selecionados:"
        for k, v in (self.controller_aev.
                     obj_para_dict("astronauta").items()):
            tooltip += f"\n{k} - {v}"
        return tooltip

    def desbloqueia_astronauta(self):
        if self.controller_aev.obj_para_dict("tarefa") is None:
            return True
        return False

    def desbloqueia_aev(self):
        if self.controller_aev.obj_para_dict("astronauta") == {}:
            return True
        return False

    def bloqueia_anomalia(self, anomalia):
        if anomalia is None:
            return False
        return True

    def iniciar_componentes(self):
        sg.ChangeLookAndFeel("Light Brown 8")

        aevs = self.dict_para_vetor(
            self.controller_aev.lista_obj_para_dict(), 'matriz')

        layout = [
            [sg.Text("Menu de AEV's",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Button("INICIAR AEV",
                       disabled=self.desbloqueia_aev(),
                       key="iniciar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Button("SELECIONAR ASTRONAUTA",
                       disabled=self.desbloqueia_astronauta(),
                       key="selec_astro",
                       tooltip=self.astronauta_selecionado(),
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Button("SELECIONAR TAREFA",
                       key="selec_tarefa",
                       tooltip=self.tarefa_selecionada(),
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 14, "bold"))],
            [sg.Text("_"*80)],
            [sg.Text("Lista de AEV's",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 15, 'bold'))],
            [sg.Text("Selecione um aev para gerar um relatório",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 15))],
            [sg.Table(aevs,
                      key="tab_aev",
                      headings=self.cabecalho,
                      max_col_width=30,
                      vertical_scroll_only=False,
                      justification='center',
                      auto_size_columns=True,
                      expand_x=True,
                      size=(0, 20),
                      font=("Gulim", 14, "bold"),
                      enable_events=True)],
            [sg.Button("↩",
                       focus=True,
                       key="voltar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 23, "bold"))],
            [sg.Button("testar")]
        ]

        self.__janela = sg.Window("SCAEV - AEV",
                                  layout, size=self.size())

    def view_aev_andamento(self):
        anomalia = None
        layout = [
            [sg.Text("AEV em andamento",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 28))],
            [sg.Button("Relatar Anomalia",
                       key="anomalia",
                       disabled=self.bloqueia_anomalia(anomalia),
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 18, "bold")),
             sg.Button("Encerrar AEV",
                       key="encerrar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 20, "bold"))]
        ]
        self.__janela = sg.Window("SCAEV - AEV em andamento", layout)
        evento, valores = self.__janela.Read()
        while True:
            if evento == "anomalia":
                valores = self.view_relatar_anomalia()
                anomalia = (valores["horario"],
                            valores["tipo"],
                            valores["descricao"])
            elif evento == "encerrar":
                break
        self.fechar()
        return anomalia

    def view_relatar_anomalia(self):
        layout = [
            [sg.Text("Relatar Anomalia",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 18))],
            [sg.Text("Tipo:",
                     expand_x=True,
                     justification='left',
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.InputText(key="tipo",
                          expand_x=True,
                          font=("Gulim", 20))],
            [sg.Text("Tempo:",
                     expand_x=True,
                     justification='left',
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.Slider(range=(0, 60),
                       key="horario",
                       expand_x=True,
                       orientation='h',
                       default_value=0)],
            [sg.Text("Descrição:",
                     justification='left',
                     expand_x=True,
                     expand_y=True,
                     font=("Gulim", 14, "bold")),
             sg.Multiline(key="descricao",
                          expand_x=True,
                          size=(40, 6),
                          font=("Gulim", 20))],
            [sg.Button("Confirmar",
                       key="confirmar",
                       expand_x=True,
                       expand_y=True,
                       font=("Gulim", 18, "bold"))]
        ]
        self.__janela = sg.Window("SCAEV - Inserir Astronauta", layout)
        evento, valores = self.__janela.Read()
        if evento == "confirmar":
            tipo = valores["tipo"]
            horario = valores["horario"]
            descricao = valores["descricao"]
            self.fechar()

            return {"tipo": tipo,
                    "horario": horario,
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

    def view_selecionar_tarefa(self, tarefas_dict: dict):
        tarefas = self.dict_para_vetor(tarefas_dict, "lista")

        layout = [
            [sg.Text("Selecione uma tarefa",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 15))],
            [sg.OptionMenu(tarefas,
                           auto_size_text=True,
                           key="tarefa",
                           expand_x=True)],
            [sg.Button("Confirmar",
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

        self.__janela = sg.Window("SCAEV - Selecionar Tarefa", layout)
        evento, valores = self.__janela.Read()

        if evento in (None, "voltar"):
            self.fechar()
            return "voltar"
        elif evento == "inserir":
            if valores["tarefa"] == "":
                self.pop_mensagem("Erro", "Selecione uma tarefa")
                self.fechar()
            else:
                codigo = valores["tarefa"][0]
                self.fechar()

                return {"codigo": codigo}

    def view_selecionar_astronautas(self, astronautas_dict: dict):
        astronautas = self.dict_para_vetor(astronautas_dict, "lista")

        layout = [
            [sg.Text("Selecione o(a) 1º astronauta",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 15))],
            [sg.OptionMenu(astronautas,
                           auto_size_text=True,
                           key="astronauta1",
                           expand_x=True)],
            [sg.Text("Selecione o(a) 2º astronauta",
                     expand_x=True,
                     justification='center',
                     font=("Gulim", 15))],
            [sg.OptionMenu(astronautas,
                           auto_size_text=True,
                           key="astronauta2",
                           expand_x=True)],
            [sg.Button("Confirmar",
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

        self.__janela = sg.Window("SCAEV - Selecionar astronauta", layout)
        evento, valores = self.__janela.Read()

        if evento in (None, "voltar"):
            self.fechar()
            return "voltar"
        elif evento == "inserir":
            if valores["astronauta1"] == "" or valores["astronauta2"] == "":
                self.pop_mensagem("Erro", "Selecione uma astronauta")
                self.fechar()
            elif valores["astronauta1"] == valores["astronauta2"]:
                self.pop_mensagem("Erro", "Selecione astronautas diferentes")
                self.fechar()
            else:
                codigo1 = valores["astronauta1"][0]
                codigo2 = valores["astronauta2"][0]
                self.fechar()

                return {"codigo_1": codigo1, "codigo_2": codigo2}

    def pega_indice_aev(self, valores):
        aev_array = []
        aev_dict = self.controller_aev.lista_obj_para_dict()
        for aev in aev_dict.values():
            aev_array.append(aev)
        linha_selecionada = valores["tab_aev"][0]
        codigo = aev_array[linha_selecionada]
        codigo = codigo.split(";")
        return int(codigo[0])

    def abrir(self):
        self.iniciar_componentes()
        evento, valores = self.__janela.Read()

        switcher = {"iniciar": 1,
                    "selec_astro": 2,
                    "selec_tarefa": 3,
                    "testar": 7}

        if evento in (None, "voltar"):
            self.fechar()
            return 0
        if evento == "tab_aev":
            self.controller_aev.gerar_relatorio(self.pega_indice_aev(valores))
            return 4

        self.fechar()
        return switcher[evento]

    def fechar(self):
        self.__janela.Close()

    def pop_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
