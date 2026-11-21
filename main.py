#Curso: Programacion 
#Edinson Stiven Gámez Cardona
#Codigo: 213023_340

from modelos.cliente import Cliente
from modelos.sala import Sala
from modelos.equipo import Equipo
from modelos.asesoria import Asesoria


def main():
    print("Sistema Integral de Gestión integral")
    #cliente valido
    print("\nREGISTRO DE CLIENTES")
    try:
        cliente1 = Cliente(1, "stiven gamez", "stiven1235@gmail.com")
        print(cliente1.mostrar_informacion())

    except ValueError as error:
        print("Error:", error)

    #cliente invalido
    try:
        cliente2 = Cliente(2, "", "correo_incorrecto")
        print(cliente2.mostrar_informacion())

    except ValueError as error:
        print("Error:", error)

    #servicios disponboles
    print("\nSERVICIOS DISPONIBLES")
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
        print("Error al crear un servicio:", error)

    #testeo de costos con impuestos y dctos.
    print("\nCALCULO DE COSTOS")

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
        print("Error en el calculo:", error)

    #prueba de un dcto. incorrecto
    print("Prueba de descuento con error")

    try:
        print(sala.calcular_costo(2, 19, 150))

    except ValueError as error:
        print("Error controlado:", error)

#ejecuta main function
if __name__ == "__main__":
    main()
