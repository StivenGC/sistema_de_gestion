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
    
    #para el contador
    exitosas = 0
    errores_controlados = 0
    
    #cliente valido
    print("Registro de Clientes")
    try:
        cliente1 = Cliente(1, "stiven gamez", "stiven1235@gmail.com")
        print(cliente1.mostrar_informacion())
        registrar_evento("cliente registrado correctamente.")
        exitosas += 1
        
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
        errores_controlados += 1

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
        exitosas += 3
    
    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)
        errores_controlados += 1

    #sala con capacidad incorrecta
    print("\nPrueba de sala con capacidad negativa")
    try:
        Sala("Sala pequena", 40000, -5)

    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)
        errores_controlados += 1

    #equipo sin tipo
    print("\nPrueba de equipo sin tipo")
    try:
        Equipo("Proyector", 20000, "")

    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)
        errores_controlados += 1

    #asesoria con precio incorrecto
    print("\nPrueba de asesoria con precio negativo")
    try:
        Asesoria("Asesoria web", -10000, "Desarrollo")

    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)
        errores_controlados += 1

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
        errores_controlados += 1
        
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
        exitosas += 1
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
        errores_controlados += 1

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
        errores_controlados += 1

    #prueba de servicio no disponible
    print("\nPrueba de servicio no disponible")
    try:
        sala.disponible = False
        Reserva(cliente, sala, 2)

    except ValueError as error:
        registrar_evento(f"ERROR: {error}")
        print("Error:", error)
        errores_controlados += 1

    finally:
        sala.disponible = True

    print("------------------------")
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

    #resumen de operaciones
    print("------------------------------")
    print("Resultados de las operaciones")
    print("Operaciones exitosas:", exitosas)
    print("Errores controlados:", errores_controlados)
    print("Total:", exitosas + errores_controlados)

    registrar_evento("Finalizaron las operaciones del sistema.")

#ejecuta main function
if __name__ == "__main__":
    main()
