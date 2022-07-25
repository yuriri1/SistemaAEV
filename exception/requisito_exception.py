class RequisitoExcepiton(Exception):
    def __init__(self, nome: str, requisito: str):
        super().__init__(f"O astronauta {nome}, " +
                         f"não atende ao requisito {requisito}")
