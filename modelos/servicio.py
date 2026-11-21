#Importo para clases abstractas
from abc import ABC, abstractmethod
#para manejo de excepciones
from excepciones.errores import ErrorServicio

#Clase abs. que representa un servicio
class Servicio(ABC):
    def __init__(self, nombre, precio_hora):
        #validacion nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("Nombre del servicio invalido.")

        #validacion precio
        if (isinstance(precio_hora, bool)
                or not isinstance(precio_hora, (int, float))
                or precio_hora <= 0):
            raise ErrorServicio("El precio debe ser mayor que cero.")

        self._nombre = nombre.strip()
        self._precio_hora = precio_hora

    #Consultar el nombre del servicio
    def obtener_nombre(self):
        return self._nombre
    #valida porcentajes de impuestos y dcto.
    def validar_porcentajes(self, impuesto, descuento):

        if (isinstance(impuesto, bool)
                or not isinstance(impuesto, (int, float))
                or impuesto < 0 or impuesto > 100):
            raise ErrorServicio("El impuesto debe estar entre 0 y 100.")

        if (isinstance(descuento, bool)
                or not isinstance(descuento, (int, float))
                or descuento < 0 or descuento > 100):
            raise ErrorServicio("El dcto. debe estar entre 0 y 100.")

    #Valida la duracion que se solicitada
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
