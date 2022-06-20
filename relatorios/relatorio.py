from cmath import e
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
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
    
    def mm2p(milimetros):
        return milimetros / 0.352777
    
    def gerar_relatorio(self):
        
        ferramentas = (self.aev.tarefa.caixa.ferramenta.ferramentas.copy())
        eixo_y = 0
        nome_ferramentas = []
        for ferramenta in ferramentas:
            nome_ferramentas.append(ferramenta.nome)
        
        dia = self.data.day
        mes = self.data.month
        ano = self.data.yea
        cnv = canvas.Canvas(f"relatorios\relatorio.pdf")
        cnv.setFont("Helvetica", 18)
        cnv.drawImage("relatorios/nasa1.png", 0,
                      self.mm2p(235), width=200, height=150)
        cnv.drawString(self.mm2p(70), self.mm2p(270),
                       "National Aeronautics and Space Administration")
        cnv.drawString(self.mm2p(70), self.mm2p(255),
                       "Houston - Texas - USA")
        cnv.drawString(self.mm2p(70), self.mm2p(240),
                       f"{dia} / {mes} / {ano}")
        cnv.line(self.mm2p(10), self.mm2p(225), self.mm2p(200), self.mm2p(225))
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


        cnv.drawString(self.mm2p(20), self.mm2p(120),
                       "ASTRONAUTAS EM MISSÃO")
        
        for astronauta in self.aev.astronautas:
            cnv.drawString(self.mm2p(20), self.mm2p(110-eixo_y),
                        f"ASTRONAUTA Nº{astronauta.codigo}")
            cnv.drawString(self.mm2p(20), self.mm2p(100-eixo_y),
                        f"{astronauta.nome}")
            cnv.drawString(self.mm2p(20), self.mm2p(90-eixo_y),
                        f"{astronauta.nacionalidade}")
            cnv.drawString(self.mm2p(20), self.mm2p(80-eixo_y),
                        f"Traje Nº{astronauta.traje.codigo} - {astronauta.traje.tipo.name} - {astronauta.traje.capacidade_o2} Litros de O2")
            eixo_y += 40
        cnv.save()

        


    

#A4 = (210*mm,297*mm)



