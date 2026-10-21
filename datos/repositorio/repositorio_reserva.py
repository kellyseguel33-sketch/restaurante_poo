from datos.modelos.reserva import Reserva
from auxiliares import mensaje_error

def listado_reservas():
    try:
        reservas = Reserva.select()
        if reservas:
            return reservas
    except Exception as error:
            print(f'{mensaje_error}{error}')

def obtener_reserva_por_id(id_reserva):
    try:
        reserva = Reserva.get(Reserva.id_reserva == id_reserva)
        if reserva:
            return reserva
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_reserva(id_restaurante, fecha, hora, cantidad_personas, id_cliente, id_estado_reserva):
    try:
        reserva = Reserva(
            id_restaurante=id_restaurante,
            fecha=fecha,
            hora=hora,
            cantidad_personas=cantidad_personas,
            id_cliente=id_cliente,
            id_estado_reserva=id_estado_reserva
        )
        reserva.save()
        if reserva:
            print('¡Reserva guardada correctamente!')
    except Exception as error:
        print(f'{mensaje_error}{error}')
