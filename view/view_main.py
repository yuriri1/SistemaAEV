class ViewMain:
    def __init__(self):
        pass
    
    def menu_inicial(self):
        print("========== SISTEMA ===========")
        print("1 - Iniciar AEV")
        print("2 - Configurar astronautas")
        print("3 - Configurar tarefa")
        print("4 - Configurar traje")
        print("5 - Configurar caixas de ferramentas")
        print("6 - Configurar ferramentas")
        print("0 - Sair")
        opcao = int(input("Opcao: "))
        return opcao