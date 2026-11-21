from modelos.servicio import Servicio

#reserva de salas
class Sala(Servicio):
    def __init__(self, nombre, precio_hora, capacidad):
        super().__init__(nombre, precio_hora)

        #Validacion de la capacidad de la sala
        if (not isinstance(capacidad, int)
                or isinstance(capacidad, bool)
                or capacidad <= 0):
            raise ValueError("La capacidad debe ser mayor a cero.")

        self.capacidad = capacidad
    #Validar las horas de reserva
    def validar_parametros(self, horas):
        if (isinstance(horas, bool)
                or not isinstance(horas, (int, float))
                or horas <= 0):
            raise ValueError("Las horas deben ser mayores que cero.")

    #calcular el valor de la reserva
    def calcular_costo(self, horas):
        self.validar_parametros(horas)
        return self._precio_hora * horas
    #Describir la sala
    def describir_servicio(self):
        return f"Sala: {self._nombre} | Capacidad: {self.capacidad} personas"
