#importo clases que se usaran
from modelos.cliente import Cliente
from modelos.servicio import Servicio

#para manejo de excepciones
from excepciones.errores import ErrorReserva
#registroe event.
from utilidades.registro import registrar_evento

#Clase para reserva
class Reserva:
    #constructor
    def __init__(self, cliente, servicio, horas):
        #validacion del cliente
        if not isinstance(cliente, Cliente):
            raise ErrorReserva("El cliente no es valido.")

        #validacion servicio
        if not isinstance(servicio, Servicio):
            raise ErrorReserva("El servicio no es valido.")

        #validacion deduracion reserva
        try:
            servicio.validar_parametros(horas)

        except ValueError as error:
            #error anterior
            raise ErrorReserva("No fue posible crear la reserva.") from error

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

        registrar_evento("Reserva creada correctamente.")

    #confirmar la reserva
    def confirmar(self):
        if self.estado == "Cancelada":
            raise ErrorReserva("No se puede confirmar una reserva cancelada.")
        
        if self.estado == "Confirmada":
            raise ErrorReserva("La reserva ya esta confirmada.")
        self.estado = "Confirmada"

        registrar_evento("Reserva confirmada correctamente.")
        print("Reserva confirmada correctamente.")
        
    #cancelar reserva
    def cancelar(self):
        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya esta cancelada.")

        self.estado = "Cancelada"

        registrar_evento("Reserva cancelada correctamente.")
        print("Reserva cancelada correctamente.")

    #procesamiento de reserva
    def procesar(self):
        if self.estado != "Confirmada":
            raise ErrorReserva("La reserva debe estar confirmada.")
        try:
            total = self.servicio.calcular_costo(self.horas)

        except ValueError as error:
            raise ErrorReserva("Error al calcular el costo de la reserva.") from error

        registrar_evento("Reserva procesada correctamente.")
        return total

    #print info. reserva
    def mostrar_informacion(self):

        return (
            f"Cliente: {self.cliente.obtener_nombre()} | "
            f"Servicio: {self.servicio.obtener_nombre()} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado}"
        )
