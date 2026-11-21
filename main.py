#Curso: Programacion 
#Edinson Stiven Gámez Cardona
#Codigo: 213023_340

from modelos.cliente import Cliente

def main():
    print(" Sistema Integral de Gestión de Clientes, Servicios y Reservas")
    print("Bienvenido")
 #Crear un cliente con datos correctos
    print("\nRegistro de cliente valido:")

    try:
        cliente1 = Cliente(1, "arnold schwarzenegger", "schwarzenegger123@gmail.com")
        print(cliente1.mostrar_informacion())

    except ValueError as error:
        print("Error:", error)

    # Intentar crear un cliente con datos incorrectos
    print("\nRegistro de cliente invalido:")

    try:
        cliente2 = Cliente(2, "", "correo_incorrecto")
        print(cliente2.mostrar_informacion())

    except ValueError as error:
        print("Error:", error)


#ejecuta main function
if __name__ == "__main__":
    main()
