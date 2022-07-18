class ListaVaziaException(Exception):
    def __init__(self, elemento: str):
        super().__init__(f"Nenhum {elemento} disponivel no sistema")
