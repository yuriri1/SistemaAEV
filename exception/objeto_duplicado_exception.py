class ObjetoDuplicadoException(Exception):
    def __init__(self, attr_duplicado: str, objeto: str):
        super().__init__(f"Não foi possível criar {objeto},\
pois ja existe {attr_duplicado} igual no sistema")