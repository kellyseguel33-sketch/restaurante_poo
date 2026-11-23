from prettytable import PrettyTable
from datos.repositorio.repositorio_reserva import listado_reservas, guardar_reserva
from datos.modelos.reserva import Reserva
from datos.modelos.mesa import Mesa
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


def obtener_mesas_disponibles(fecha, hora):
    try:
        # Corregido: Se envuelven todas las condiciones correctamente dentro del .where(...)
        mesas_ocupadas_ids = (
            Reserva.select(Reserva.id_mesa)
            .where(
                (Reserva.fecha == fecha) & 
                (Reserva.hora == hora) & 
                (Reserva.id_mesa.is_null(False))
            )
        ) 
        ids_ocupados = [r.id_mesa for r in mesas_ocupadas_ids]

        # Si hay mesas ocupadas, las filtramos; si no, trae todas las mesas
        if ids_ocupados:
            mesas_disponibles = Mesa.select().where(~Mesa.id_mesa.in_(ids_ocupados))
        else:
            mesas_disponibles = Mesa.select()
            
        return mesas_disponibles
    except Exception as error:
        print(f'Error al consultar mesas disponibles: {error}')
        return []


def crear_objeto_reserva(fecha, hora: str, cantidad_personas: int, id_restaurante: int, id_cliente: int, id_mesa: int, id_estado_reserva: int):
    try:
        guardar_reserva(
            id_restaurante=id_restaurante,
            fecha=fecha,
            hora=hora,
            cantidad_personas=cantidad_personas,
            id_cliente=id_cliente,
            id_estado_reserva=id_estado_reserva,
            id_mesa=id_mesa
        )
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_reserva(fecha, hora: str, cantidad_personas: int, id_restaurante: int, id_cliente: int, id_mesa: int, id_estado_reserva: int, reserva: Reserva):
    try:
        if fecha != '':
            reserva.fecha = fecha
        if hora != '':
            reserva.hora = hora
        if cantidad_personas != '':
            reserva.cantidad_personas = cantidad_personas
        if id_restaurante != '':
            reserva.id_restaurante = id_restaurante
        if id_cliente != '':
            reserva.id_cliente = id_cliente
        if id_mesa != '':
            reserva.id_mesa = id_mesa
        if id_estado_reserva != '':
            reserva.id_estado_reserva = id_estado_reserva
            
        reserva.save()
        print('¡Reserva actualizada correctamente!')
    except Exception as error:
        print(f'{mensaje_error}{error}')