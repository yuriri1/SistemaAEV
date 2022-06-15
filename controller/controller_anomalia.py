from model.anomalia import Anomalia
from view.view_anomalia import ViewAnomalia

class ControllerAnomalia:
    def __init__(self,controller_main):
        self.__anomalias = []
        self.__view_anomalia = ViewAnomalia()
    
    