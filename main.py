#Curso: Programacion 
#Edinson Stiven Gámez Cardona
#Codigo: 213023_340

from modelos.cliente import Cliente
from modelos.sala import Sala
from modelos.equipo import Equipo

from modelos.asesoria import Asesoria
from modelos.reserva import Reserva

from utilidades.registro import registrar_evento


def main():
    print("Sistema Integral de Gestión integral")
    #cliente valido
    print("Registro de Clientes")
    try:
        cliente1 = Cliente(1, "stiven gamez", "stiven1235@gmail.com")
        print(cliente1.mostrar_informacion())

    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)

    #cliente invalido
    try:
        cliente2 = Cliente(2, "", "correo_incorrecto")
        print(cliente2.mostrar_informacion())

    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)

    #servicios disponboles
    print("\nServicios Disponibles")
    try:
        sala = Sala("Sala de reuniones", 50000, 10)
        equipo = Equipo("Computador portatil", 30000, "Tecnologia")
        asesoria = Asesoria("Asesoria de php", 80000, "Programacion")
        #Lista de objetos, es para diferentes clases
        servicios = [sala, equipo, asesoria]
        for servicio in servicios:
            print("\n" + servicio.describir_servicio())
            print("Costo por 2 horas: $", servicio.calcular_costo(2))
    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)

    #testeo de costos con impuestos y dctos.
    print("\nCalculo de costos")

    try:
        sala = Sala("Sala de reuniones", 50000, 10)

        #costo sin impuesto ni descto.
        print("Costo normal:", sala.calcular_costo(2))
        #costo con +19%
        print("Costo con impuesto:", sala.calcular_costo(2, 19))
        # Costo con +19% y dcto.
        print("Costo con impuesto y descuento:",
              sala.calcular_costo(2, 19, 10))

    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)

    #prueba de un dcto. incorrecto
    print("Prueba de descuento con error")
    try:
        print(sala.calcular_costo(2, 19, 150))
    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)
        
    print("------------------------------")    
    print("Gestion de las reservas")
    #creear reserva con info. correcta
    try:
        cliente = Cliente(3, "Stiven Cardona", "stivencar12345@gmail.com")
        sala = Sala("Sala de reuniones", 50000, 10)

        reserva1 = Reserva(cliente, sala, 3)

        print("\nReserva creada:")
        print(reserva1.mostrar_informacion())

        #confirmar
        reserva1.confirmar()

        #procesar y calcular costo
        total = reserva1.procesar()
        print("Costo total: $", total)

        print(reserva1.mostrar_informacion())
    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)

    #reserva con horas invalidas
    print("Test con errores controlados")

    try:
        reserva2 = Reserva(cliente, sala, -2)
        print(reserva2.mostrar_informacion())
    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)

    #Cancelar reserva
    print("Cancelacion de reserva")
    try:
        reserva1.cancelar()
        print(reserva1.mostrar_informacion())
    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)

    #Intento de confirmar reserva cancelada
    print("Prueba de conexion invalida")

    try:
        reserva1.confirmar()
    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)


    print("\nTesteo de excepciones")
    try:
        #reserva valida
        cliente = Cliente(4, "Edinson Gamez", "edgamez12345@gmail.com")
        equipo = Equipo("Computador", 30000, "Portatil")

        reserva = Reserva(cliente, equipo, 2)
        reserva.confirmar()

        total = reserva.procesar()

    except ValueError as error:
        print("Error:", error)
        registrar_evento(f"ERROR: {error}")

    else:
        print("Operacion existosa.")
        print("Total de la reserva: $", total)
        registrar_evento("Operacion finalizada sin errores.")

    finally:
        #Se ejecuta aunque ocurra un error
        print("Finalizo la operacion.")
        registrar_evento("FIn prueba.")

#ejecuta main function
if __name__ == "__main__":
    main()
