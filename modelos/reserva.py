#importo clases que se usaran
from modelos.cliente import Cliente
from modelos.servicio import Servicio


#Clase para reserva
class Reserva:
    #constructor
    def __init__(self, cliente, servicio, horas):
        #validacion cliente
        if not isinstance(cliente, Cliente):
            raise ValueError("El cliente no es valido.")
        #validacion servicio
        if not isinstance(servicio, Servicio):
            raise ValueError("El servicio es invalido.")
        #validacion de las horas utilizando el metodo del servicio
        servicio.validar_parametros(horas)
        #guardado
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    #metodo confirmar reserva
    def confirmar(self):
        if self.estado == "Cancelada":
            raise ValueError("No se puede confirmar una reserva cancelada.")
        if self.estado == "Confirmada":
            raise ValueError("La reserva ya esta confirmada.")
        self.estado = "Confirmada"
        print("Reserva confirmada correctamente.")

    #metodo cancelar reserva
    def cancelar(self):
        if self.estado == "Cancelada":
            raise ValueError("La reserva ya esta cancelada.")
        self.estado = "Cancelada"
        print("Reserva cancelada correctamente.")

    #metodo para procesar reserva
    def procesar(self):
        #Solo se procesaran reservas confirmadas
        if self.estado != "Confirmada":
            raise ValueError("La reserva debe estar confirmada.")
        #calculo del valor total
        total = self.servicio.calcular_costo(self.horas)

        return total

    #Metodo para mostrar informacion
    def mostrar_informacion(self):
        return (
            f"Cliente: {self.cliente.obtener_nombre()} | "
            f"Servicio: {self.servicio.obtener_nombre()} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado}"
        )
