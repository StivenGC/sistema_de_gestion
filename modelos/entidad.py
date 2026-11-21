#Importo para clases abstractas
from abc import ABC, abstractmethod

#Clase abstracta para representar entidad.
class Entidad(ABC):

    #Constructor que recibe
    def __init__(self, identificador):
        self._identificador = identificador

    #Metodo para consultar identificador
    def obtener_identificador(self):
        return self._identificador

    #Metodo que implementar las subclases/clases hijas
    @abstractmethod
    def mostrar_informacion(self):
        pass
