#Importo para clases abstractas
from abc import ABC, abstractmethod

#Clase abs. que representa un servicio
class Servicio(ABC):

    def __init__(self, nombre, precio_hora):

        #validacion nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre del servicio invalido.")

        #validacion precio
        if (isinstance(precio_hora, bool)
                or not isinstance(precio_hora, (int, float))
                or precio_hora <= 0):
            raise ValueError("El precio debe ser mayor que cero.")

        self._nombre = nombre.strip()
        self._precio_hora = precio_hora

    #Consultar el nombre del servicio
    def obtener_nombre(self):
        return self._nombre

    # Validar la duracion solicitada
    @abstractmethod
    def validar_parametros(self, horas):
        pass

    #Calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    #mostrar la descripcion del servicio
    @abstractmethod
    def describir_servicio(self):
        pass
