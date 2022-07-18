class RequisitoExcepiton(Exception):
    def __init__(self, requisito: str):
        super().__init__(f'''Esse astronauta não atende ao
requisito de {requisito}''')
