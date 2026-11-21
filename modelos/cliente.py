#se importa la clase Entidad
from modelos.entidad import Entidad

#Clase cliente que hereda de Entidad
class Cliente(Entidad):
    #constructor del cliente
    def __init__(self, identificador, nombre, correo):
        #validacion del identificador
        if not isinstance(identificador, int) or isinstance(identificador, bool) or identificador <= 0:
            raise ValueError("El identificador debe ser mayor a cero.")

        #validacion del nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")

        # validacion del correo
        if not isinstance(correo, str) or "@" not in correo or "." not in correo.split("@")[-1]:
            raise ValueError("El correo electronico no es valido.")

        #llamada al constructor de la clase padre
        super().__init__(identificador)

        #guardar datos del cliente
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()

    #Metodo para consultar el nombre
    def obtener_nombre(self):
        return self.__nombre

    #Metodo para consultar el correo
    def obtener_correo(self):
        return self.__correo

    #implementacion del metodo abstracto
    def mostrar_informacion(self):
        return (
            f"ID: {self.obtener_identificador()} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo}"
        )
