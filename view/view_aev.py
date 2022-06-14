from view.abstract_view import AbstractView

class ViewAEV(AbstractView):
    def __init__(self):
        pass
    
    
    def view_opcoes(self):
        print("MENU INICIAL ---> MENU DO AEV")
        print("1 - Selecionar Astronautas")
        print("2 - Selecionar Tarefa")
        print("3 - Iniciar AEV")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha uma opção: ",[1, 2, 3, 0])
        return opcao
    
    def listar_tarefas(self, tarefas: list):
        print("MENU INICIAL --> MENU DO AEV")
        print("Selecione a tarefa: ")
        for num, tarefa in enumerate(tarefas):
            print(str(num) + " - "+tarefa.titulo)
        
        tarefa_selecionada = self.le_num_inteiro("Escolha a tarefa: ",tarefas)
        return tarefa_selecionada 
       
    def listar_astronautas(self):
        pass
         # qnt_astronauta = input("Quantos astronautas para a AEV: ")
        
        # astro = []
        # for i in range(qnt_astronauta):
        #     for num, astronauta in enumerate(astronautas):
        #         print(num+" - "+astronauta.nome)
        #     astro.append(int(input(("Selecione o astronauta pelo número: "))))
    
    def view_relatar_anomalia(self):
        print("MENU INICIAL --> MENU DO AEV --> AEV EM EXECUÇÃO --> RELATANDO ANOMALIA")
        horario = input("Quando ocorreu a anomalia: ")
        tipo = input("Tipo da anomalia: ")
        descricao = input("Descreva a ocorrencia: ")
        return horario, tipo, descricao
        