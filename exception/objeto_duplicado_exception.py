class ObjetoDuplicadoException(Exception):
    def __init__(self, objeto: str):
        super().__init__(f"Não foi possível criar {objeto},\
pois ja existe um com o codigo igual no sistema")
