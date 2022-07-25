from abc import ABC, abstractmethod
# import PySimpleGUI as sg


class AbstractView(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def size(self):
        return (600, 800)

    def dict_para_matriz(self, dicionario: dict):
        matriz = []
        for chave, valor in dicionario.items():
            matriz.append([chave, valor])
        return matriz

    def view_incluir(self):
        pass

    def view_editar(self):
        pass

    # def le_num_inteiro(self, mensagem: str, inteiros_validos: list = None):
    #     while True:
    #         valor_lido = input(mensagem)
    #         try:
    #             inteiro = int(valor_lido)
    #             if inteiros_validos and inteiro not in inteiros_validos:
    #                 raise ValueError
    #             return inteiro
    #         except ValueError:
    #             print("Valor incorreto.")
    #             print("Digite um valor numerico inteiro valido")
    #             if inteiros_validos:
    #                 print("Valores validos: ",
    #                       ', '.join([str(i) for i in inteiros_validos]))

    # def le_num_inteiro_limitado(self, mensagem: str, limite: int):
    #     while True:
    #         valor_lido = input(mensagem)
    #         try:
    #             inteiro = int(valor_lido)
    #             if inteiro > limite:
    #                 raise ValueError
    #             return inteiro
    #         except ValueError:
    #             print("Valor maior do que o permitido")
    #             if limite:
    #                 print(f"Valores validos: 1 até {limite}")

    # def le_num_flutuante(self, mensagem: str):
    #     while True:
    #         valor_lido = input(mensagem)
    #         try:
    #             flutuante = float(valor_lido)
    #             if not (isinstance(flutuante, float)):
    #                 raise ValueError
    #             return flutuante
    #         except ValueError:
    #             print("Valor incorreto.")
    #             print("Digite um valor numerico flutuante valido")

    # def view_mensagem(self, msg: str):
    #     print(msg)

    # def view_codigos(self, codigos: list = None,
    #                  objeto: str = None,
    #                  acao: str = None):
    #     if codigos is None:
    #         return self.le_num_inteiro(f"Codigo {objeto}: ")

    #     return self.le_num_inteiro(
    #             f"Escreva o codigo do {objeto} que deseja {acao}:",
    #             codigos)
