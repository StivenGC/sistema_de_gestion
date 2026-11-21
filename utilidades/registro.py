#usare datetime para fecha y hora
from datetime import datetime

#Funcion que registra eventos y errores
def registrar_evento(mensaje):
    #se obtiene fecha y hora
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #abrir el en modo agregar y guarda el mensaje
    with open("registro.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {mensaje}\n")
