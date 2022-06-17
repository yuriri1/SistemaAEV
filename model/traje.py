from model.tipo_traje import TipoTraje

class Traje:
    def __init__(self,codigo: int,tipo: TipoTraje,capacidade_o2: float):
        self.__codigo = codigo
        self.__tipo = tipo
        self.__capacidade_o2 = capacidade_o2
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: TipoTraje):
        self.__tipo = tipo
        
    @property
    def capacidade_o2(self):
        return self.__capacidade_o2
    
    @capacidade_o2.setter
    def capacidade_o2(self, capacidade_o2: float):
        self.__capacidade_o2 = capacidade_o2