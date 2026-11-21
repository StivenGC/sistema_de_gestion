#Excepciones personalizadas para el proyecto

#Errores clientes
class ErrorCliente(ValueError):
    pass #indicador para no agregar codigo


#Errores servicios
class ErrorServicio(ValueError):
    pass


#Errores reservas
class ErrorReserva(ValueError):
    pass
