from modelos.servicio import Servicio

#alquiler de equipos
class Equipo(Servicio):
    def __init__(self, nombre, precio_hora, tipo_equipo):
        super().__init__(nombre, precio_hora)

        # validacion del tipo de equipo
        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ValueError("El tipo de equipo no es valido.")

        self.tipo_equipo = tipo_equipo.strip()

    #Validar las horas de alquiler
    def validar_parametros(self, horas):
        if (isinstance(horas, bool)
                or not isinstance(horas, (int, float))
                or horas <= 0):
            raise ValueError("Las horas deben ser mayores que cero.")

    #Calcular el costo del alquiler
    def calcular_costo(self, horas):
        self.validar_parametros(horas)
        return self._precio_hora * horas

    #Describir el equipo
    def describir_servicio(self):
        return f"Equipo: {self._nombre} | Tipo: {self.tipo_equipo}"
