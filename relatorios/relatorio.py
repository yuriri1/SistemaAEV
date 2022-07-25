from reportlab.pdfgen import canvas
import datetime


class Relatorio():
    def __init__(self, aev):
        self.__aev = aev
        self.__data = datetime.datetime.now()

    @property
    def aev(self):
        return self.__aev

    @aev.setter
    def aev(self, aev):
        self.__aev = aev

    @property
    def data(self):
        return self.__data

    def mm2p(self, milimetros):
        return milimetros / 0.352777

    def gerar_relatorio(self):

        ferramentas = (self.aev.tarefa.caixa.ferramentas.copy())
        print(tarefas)
        nome_ferramentas = []
        for ferramenta in ferramentas:
            nome_ferramentas.append(ferramenta.nome)
        dia = self.data.day
        mes = self.data.month
        ano = self.data.year
        cnv = canvas.Canvas(f"relatorio{self.aev.codigo}.pdf")
        cnv.setFont("Helvetica", 18)
        cnv.drawImage("relatorios/nasa1.png", 0,
                      self.mm2p(235), width=200, height=150)
        cnv.drawString(self.mm2p(70), self.mm2p(270),
                       "National Aeronautics and Space Administration")
        cnv.drawString(self.mm2p(70), self.mm2p(255),
                        "Houston - Texas - USA")
        cnv.drawString(self.mm2p(70), self.mm2p(240),
                        f"{dia} / {mes} / {ano}")
        cnv.line(self.mm2p(10), self.mm2p(225),
                    self.mm2p(200), self.mm2p(225))
        cnv.drawString(self.mm2p(20), self.mm2p(210),
                       f"RELATÓRIO DE MISSÃO AEV Nº {self.aev.codigo}")
        cnv.drawString(self.mm2p(20), self.mm2p(190),
                        "TAREFA REALIZADA")
        cnv.drawString(self.mm2p(20), self.mm2p(180),
                        f"{self.aev.tarefa.titulo}")
        cnv.drawString(self.mm2p(20), self.mm2p(170),
                        f"{self.aev.tarefa.descricao}")
        cnv.drawString(self.mm2p(20), self.mm2p(160),
                        "CAIXA UTILIZADA:")
        cnv.drawString(self.mm2p(20), self.mm2p(150),
                        f"{self.aev.tarefa.caixa.nome} c/ {', '.join(nome_ferramentas)}")
        cnv.drawString(self.mm2p(20), self.mm2p(140),
                        f"{self.aev.tarefa.duracao} minutos")
        # cnv.drawString(self.mm2p(20), self.mm2p(120),
        #                 "ASTRONAUTAS EM MISSÃO")
        # if len(self.aev.astronautas) == 1:
        #     cnv.drawString(self.mm2p(20), self.mm2p(110),
        #                     f"ASTRONAUTA Nº{self.aev.astronautas[0].codigo}")
        #     cnv.drawString(self.mm2p(20), self.mm2p(100),
        #                     f"{self.aev.astronautas[0].nome}")
        #     cnv.drawString(self.mm2p(20), self.mm2p(90),
        #                     f"{self.aev.astronautas[0].nacionalidade}")
        #     cnv.drawString(self.mm2p(20), self.mm2p(80),
        #                     f"Traje Nº{self.aev.astronautas[0].traje.codigo} - {self.aev.astronautas[0].traje.tipo.name} - {self.aev.astronautas[0].traje.capacidade_o2} Litros de O2")
        # elif len(self.aev.astronautas) == 2:
        #     cnv.drawString(self.mm2p(20), self.mm2p(70), f"ASTRONAUTA Nº{self.aev.astronautas[1].codigo}")
        #     cnv.drawString(self.mm2p(20), self.mm2p(60), f"{self.aev.astronautas[1].nome}")
        #     cnv.drawString(self.mm2p(20), self.mm2p(50), f"{self.aev.astronautas[1].nacionalidade}")
        #     cnv.drawString(self.mm2p(20), self.mm2p(40), f"Traje Nº{self.aev.astronautas[1].traje[0].codigo} - {self.aev.astronautas[0].traje.tipo.name} - {self.aev.astronautas[0].traje.capacidade_o2} Litros de O2")        
        cnv.save()
