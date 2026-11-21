from modelos.servicio import Servicio

#servcio de asesorias especializadas
class Asesoria(Servicio):
    def __init__(self, nombre, precio_hora, especialidad):
        super().__init__(nombre, precio_hora)
        #validacion de especialidad
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad no es valida.")

        self.especialidad = especialidad.strip()

    #validar las horas de asesoria
    def validar_parametros(self, horas):
        if (isinstance(horas, bool)
                or not isinstance(horas, (int, float))
                or horas <= 0):
            raise ValueError("Las horas deben ser mayores que cero.")

    #calcular el costo de la asesoria
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        self.validar_parametros(horas)
        self.validar_porcentajes(impuesto, descuento)
        subtotal = self._precio_hora * horas
        valor_descuento = subtotal * descuento / 100
        subtotal_descuento = subtotal - valor_descuento
        valor_impuesto = subtotal_descuento * impuesto / 100
        total = subtotal_descuento + valor_impuesto
        return round(total, 2)

    #describir la asesoria
    def describir_servicio(self):
        return f"Asesoria: {self._nombre} | Especialidad: {self.especialidad}"
