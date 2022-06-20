from enum import Enum

class TipoTraje(Enum):
    Intraveicular = 1
    Extraveicular = 2
    
print(TipoTraje.Extraveicular.value)