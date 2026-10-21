from prettytable import PrettyTable
from datos.repositorio.repositorio_reserva import listado_reservas, guardar_reserva
from datos.modelos.reserva import Reserva
from auxiliares import mensaje_error


def procesar_listado_reservas(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'Fecha', 'Hora', 'Personas', 'Restaurante', 'Cliente', 'Mesa', 'Estado']
        lista_reservas = listado_reservas()
        if lista_reservas:
            for reserva in lista_reservas:
                tabla.add_row([
                    reserva.id_reserva,
                    reserva.fecha,
                    reserva.hora,
                    reserva.cantidad_personas,
                    reserva.id_restaurante,
                    reserva.id_cliente,
                    reserva.id_mesa,
                    reserva.id_estado_reserva
                ])
            return tabla


def crear_objeto_reserva(fecha, hora: str, cantidad_personas: int, id_restaurante: int, id_cliente: int, id_mesa: int, id_estado_reserva: int):
    try:
        reserva = Reserva(
            fecha=fecha,
            hora=hora,
            cantidad_personas=cantidad_personas,
            id_restaurante=id_restaurante,
            id_cliente=id_cliente,
            id_mesa=id_mesa,
            id_estado_reserva=id_estado_reserva
        )
        guardar_reserva(reserva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_reserva(fecha, hora: str, cantidad_personas: int, id_restaurante: int, id_cliente: int, id_mesa: int, id_estado_reserva: int, reserva: Reserva):
    try:
        if reserva.fecha != fecha and fecha != '':
            reserva.fecha = fecha
        if reserva.hora != hora and hora != '':
            reserva.hora = hora
        if reserva.cantidad_personas != cantidad_personas and cantidad_personas != '':
            reserva.cantidad_personas = cantidad_personas
        if reserva.id_restaurante != id_restaurante and id_restaurante != '':
            reserva.id_restaurante = id_restaurante
        if reserva.id_cliente != id_cliente and id_cliente != '':
            reserva.id_cliente = id_cliente
        if reserva.id_mesa != id_mesa and id_mesa != '':
            reserva.id_mesa = id_mesa
        if reserva.id_estado_reserva != id_estado_reserva and id_estado_reserva != '':
            reserva.id_estado_reserva = id_estado_reserva
            
        guardar_reserva(reserva)
    except Exception as error:
        print(f'{mensaje_error}{error}')